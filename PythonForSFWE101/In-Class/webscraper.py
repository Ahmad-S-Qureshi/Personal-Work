import requests
from bs4 import BeautifulSoup
import os
import random
from threading import Thread
import time
from thread_manager import thread_manager




class webscraper:
    def __init__(self):
        pass

    def get_images(self):
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
                manager = thread_manager(URL_list, query = query)
                t1 = Thread(manager.makeThreads(), daemon=True)
                t1.start()
                
                time.sleep(1)
            
            try:
                manager.killThreads = True
            except:
                pass
