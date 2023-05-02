import os
from threading import Thread
from time import time
from requests import get as get_request
from bs4 import BeautifulSoup
from PIL import Image

class thread_manager:
    def __init__(self, URLS_to_do = [], linesDone = 0, URLS_completed = [], threadList = [], query = "", killThreads = False, startTime = int(time())):
        self.URLS_to_do = URLS_to_do
        self.linesDone = linesDone
        self.URLS_completed = URLS_completed
        self.threadList = threadList
        self.query = query
        self.killThreads = killThreads
        self.startTime = startTime

    def makeThreads(self):
        for website in self.URLS_to_do:
            t1 = Thread(target=grabDataFromWebsite, args=(website, self.query, self), daemon=True)
            t1.start()
            self.threadList.append(t1)

def grabDataFromWebsite(website, query, threadManager):
    if(website not in threadManager.URLS_completed and len(os.listdir(os.path.join(os.curdir, "images")))<50):
        connected = False
        tries = 0
        r=None
        while(not connected and not threadManager.killThreads):
            try:
                if(tries<3):
                    r = get_request(website, timeout=1.5)
                    connected = True
                else:
                    break
            except:
                #print("connect failed, trying again")
                tries+=1
        if (r!=None):
            soup = BeautifulSoup(r.content, 'html5lib') 
            pretty_data = soup.prettify()
            lines = pretty_data.split('\n')
            for line in lines:
                if("https" in line and "image" in line):
                    try:
                        image_url = line.split("\"")[1]
                    except:
                        break

                    if "https" in image_url and "slideshare" not in image_url and (len(os.listdir(os.path.join(os.curdir, "images")))<50) and (threadManager.killThreads == False) and threadManager.linesDone<20:
                        threadManager.linesDone+=1
                        try:
                            img_data = get_request(image_url, timeout=1.5).content
                            with open(os.path.join(os.curdir, "images", query+ str(threadManager.linesDone)+'.jpg'), 'wb') as handler:
                                handler.write(img_data)
                                path = os.path.join(os.curdir, "images", query+ str(threadManager.linesDone)+'.jpg')
                                print(website)
                                threadManager.URLS_completed.append(website)
                            with open(path, 'r') as handler:
                                text = handler.read()
                                if(("js" in text) or ("return" in text) or ("css" in text) or (text == '') or ("") or ("<head>" in text)):
                                    os.remove(query+ str(threadManager.linesDone)+'.jpg')
                            
                            image = Image.open(path)
                            if(image.height > 80 and image.height > 80):
                                new_image = image.resize((100, 100))
                                new_image.save(path)
                            else:
                                os.remove(path)

                            
                            
                                
                        except:
                            pass