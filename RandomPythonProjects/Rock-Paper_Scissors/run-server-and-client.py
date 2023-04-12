import os
import asyncio
import time
import threading

def start_server():
    os.system("python3 server.py")

def start_client():
    os.system("python3 client.py")


with open("running.txt", "w") as handler:
    handler.write("false")

t1 = threading.Thread(target=start_server)
t1.start()
curr_state = "false"
while(curr_state == "false"):
    with open("running.txt", "r") as handler:
        curr_state = handler.read()
        print("not set up yet")
        time.sleep(1)
t2 = threading.Thread(target=start_client)
t2.start()

