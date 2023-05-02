from requests import get as get_data
from bs4 import BeautifulSoup
from os import path, remove, curdir
from random import choice
import threading
from time import time, sleep


# Ahmad's EPIC Webscraper

# Grabs images and stores into the ./images folder
def get_images():
    
    # Sets queries to be googled
    queries = ["ghost", "fighter+jet", "evil+monster", "dragon", "evil+robot", "alien", "dark+knight",  "necromancer+humanoid", "orc+horde", "shadow+assassin", "skeleton+army", "space+warship", "superpowered+villain", "undead+army"]

    # Picks a random query and displays that it is starting
    query = choice(queries)
    print("Starting query " + query)

    # Prepares a URL list for all images
    tempURL_list = []

    # Prepares a URL list for verified images
    URL_list = []

    # Grabs data from google
    r = get_data("https://www.google.com/search?q=" + query +"+4k&client=ubuntu-sn&hs=Gpk&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjx_Lz9uYL-AhVyLUQIHQN6ChEQ0pQJegQIAxAC&biw=1846&bih=968&dpr=1#imgrc=hQb-oUtO6irbwM")
    
    # Cleans up request from URL
    soup = BeautifulSoup(r.content, 'html5lib') 
    pretty_data = soup.prettify()

    # Splits into websites within the html data
    lines = pretty_data.split('/url?q=')
    for line in lines:
        line = line.split("\n")
    for line in lines:
        # Grabs not google links
        if(("google" not in line) and ("https://" in line)):
            tempURL_list.append(line.split("\"")[0])

    # Appends finalized list
    for website in tempURL_list:
        URL_list.append(website.split("&amp")[0])

    # Starts threads to make many requests at once
    manager = threadManager(URL_list, query = query)
    t1 = threading.Thread(manager.makeThreads(), daemon=True)
    t1.start()

    # Closes webscraper after 20 seconds to prevent too much data
    sleep(20)
    print("ending webscraper")

class threadManager:
    def __init__(self, URLS_to_do = [], linesDone = 0, URLS_completed = [], threadList = [], query = "", killThreads = False, startTime = int(time())):
        # List of URLS to resolve into images
        self.URLS_to_do = URLS_to_do

        # Stores number of images from the site to prevent too many
        self.linesDone = linesDone

        # Prevents a URL from being used twice (some images were used twice because of one website having it more than once)
        self.URLS_completed = URLS_completed
        self.threadList = threadList
        self.query = query

        # Variable to kill all threads
        self.killThreads = killThreads
        self.startTime = startTime

    # Makes a million threads to open and grab data from each website
    def makeThreads(self):
        for website in self.URLS_to_do:
            t1 = threading.Thread(target=grabDataFromWebsite, args=(website, self.query, self), daemon=True)
            t1.start()
            self.threadList.append(t1)

# Actually grabs data from not google
def grabDataFromWebsite(website, query, threadManager):
    if(website not in threadManager.URLS_completed):
        # Prepares variables for running
        connected = False
        tries = 0
        r=None

        # Grabs data if the thread isn't dead and the website hasn't been connected to
        while(not connected and not threadManager.killThreads):
            try:
                if(tries<3):
                    r = get_data(website, timeout=1.5)
                    connected = True
                else:
                    break
            except:
                tries+=1

        # If connection successful, grabs data
        if (r!=None):

            # Grabs data from the request
            soup = BeautifulSoup(r.content, 'html5lib') 
            pretty_data = soup.prettify()
            lines = pretty_data.split('\n')

            # If the line is a link to an image, stores said image
            for line in lines:
                if("https" in line and "image" in line):
                    try:
                        image_url = line.split("\"")[1]
                    except:
                        break
                    
                    # Grabs data if actually a link and if the link isn't slideshare (a boring site with far too many images)
                    if "https" in image_url and "slideshare" not in image_url and threadManager.linesDone<150 and threadManager.killThreads == False:
                        threadManager.linesDone+=1
                        try:
                            # Grabs image data
                            img_data = get_data(image_url, timeout=1.5).content

                            # stores images and marks link as completed
                            with open(path.join(curdir, "images", query+ str(threadManager.linesDone)+'.jpg'), 'wb') as handler:
                                handler.write(img_data)
                                #print(website)
                                threadManager.URLS_completed.append(website)
                            
                            # Removes some broken images, further work done later
                            with open(path.join(curdir, "images", query+ str(threadManager.linesDone)+'.jpg'), 'r') as handler:
                                text = handler.read()
                                if("js" in text or "return" in text or "css" in text or text == '' or path.getsize("./images/"+query+ str(threadManager.linesDone)+'.jpg')<10000000):
                                    remove(query+ str(threadManager.linesDone)+'.jpg')
                                else:
                                    break
                                
                        except:
                            pass
        
