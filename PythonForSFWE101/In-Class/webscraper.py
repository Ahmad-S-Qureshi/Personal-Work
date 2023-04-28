import requests
from bs4 import BeautifulSoup
import os
import random
import threading
import time





def get_images():
    while(True):  
        while(len(os.listdir(os.path.join(os.curdir, "images")))<50):
            queries = ["kiwi", 'lemon', 'lime', 'watermelon', 'orange+cirtus',"passionfruit",'blueberry','raspberry','blueberry',"guava","papaya", 'coconut', 'banana', 'apple', 'guava', 'huckleberry', 'pumpkin', 'elderberry', 'raisin', 'dragonfruit', 'nectarine', 'pear', 'kumquat']
            query = random.choice(queries)
            print("Starting query " + query)
            tempURL_list = []
            URL_list = []
            r = requests.get("https://www.google.com/search?q=cartoon+" + query +"+fruit+720p&client=ubuntu-sn&hs=Gpk&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjx_Lz9uYL-AhVyLUQIHQN6ChEQ0pQJegQIAxAC&biw=1846&bih=968&dpr=1#imgrc=hQb-oUtO6irbwM")
            soup = BeautifulSoup(r.content, 'html5lib') 
            pretty_data = soup.prettify()
            lines = pretty_data.split('/url?q=')
            for line in lines:
                line = line.split("\n")
            for line in lines:
                if(("google" not in line) and ("https://" in line)):
                    tempURL_list.append(line.split("\"")[0])

            for website in tempURL_list:
                URL_list.append(website.split("&amp")[0])
            manager = threadManager(URL_list, query = query)
            t1 = threading.Thread(manager.makeThreads(), daemon=True)
            t1.start()
            
            time.sleep(1)
        
        try:
            manager.killThreads = True
        except:
            pass

class threadManager:
    def __init__(self, URLS_to_do = [], linesDone = 0, URLS_completed = [], threadList = [], query = "", killThreads = False, startTime = int(time.time())):
        self.URLS_to_do = URLS_to_do
        self.linesDone = linesDone
        self.URLS_completed = URLS_completed
        self.threadList = threadList
        self.query = query
        self.killThreads = killThreads
        self.startTime = startTime

    def makeThreads(self):
        for website in self.URLS_to_do:
            t1 = threading.Thread(target=grabDataFromWebsite, args=(website, self.query, self), daemon=True)
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
                    r = requests.get(website, timeout=1.5)
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

                    if "https" in image_url and "slideshare" not in image_url and (len(os.listdir(os.path.join(os.curdir, "images")))<50) and (threadManager.killThreads == False):
                        threadManager.linesDone+=1
                        try:
                            img_data = requests.get(image_url, timeout=1.5).content
                            with open(os.path.join(os.curdir, "images", query+ str(threadManager.linesDone)+'.jpg'), 'wb') as handler:
                                handler.write(img_data)
                                path = os.path.join(os.curdir, "images", query+ str(threadManager.linesDone)+'.jpg')
                                #print(website)
                                threadManager.URLS_completed.append(website)
                            with open(path, 'r') as handler:
                                text = handler.read()
                                if(("js" in text) or ("return" in text) or ("css" in text) or (text == '') or (os.path.getsize(path)<10000000000) or ("<head>" in text)):
                                    os.remove(query+ str(threadManager.linesDone)+'.jpg')
                                else:
                                    break
                                
                        except:
                            pass