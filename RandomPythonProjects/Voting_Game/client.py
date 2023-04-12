import websockets
import asyncio
import sys
import os
import pygame
from threading import Thread
from pygame.locals import *
import tkinter as tk
from time import sleep

#sys.stderr = open(os.devnull, "w")

def set_ip(input_IP_button):
    global IP
    IP = input_IP_button.get()
    print(IP)




def get_ip():
    window = tk.Tk()
    greeting = tk.Label(text="Enter IP and close this Window")
    greeting.pack()
    window.update()
    IP_Input = tk.Entry(bg="purple", fg = "yellow",  width=50)
    IP_Input.insert(0, '0')
    IP_Input.pack()
    IP_input_button = tk.Button(text= "Set IP", width=20, height=1, bg = "blue", fg = "yellow", command = lambda:set_ip(IP_Input))
    IP_input_button.pack(side=tk.LEFT)
    window.update()
    window.mainloop()
    
            



# Draws centered text a bit less painfully
def drawCenteredText(text, background, font, height, screen):
    tempText = font.render(text, 1, (180, 180, 180))
    tempTextRect = tempText.get_rect()
    tempTextPos = Rect(0, height, tempTextRect.w, tempTextRect.h)
    centerXPos = background.get_rect().centerx
    tempTextPos.centerx = centerXPos
    background.blit(tempText, tempTextPos)
    screen.blit(background, (0,0))


# The main function that will handle connection and communication 
# with the server
async def listen():
    global IP
    print("checking IP")
    #IP = input("Enter server IP: ")
    url = f"ws://{IP}:4206"
    name = ""
    # Connect to the server
    async with websockets.connect(url, ping_interval = 1) as ws:
        # Send a greeting message
        first_connected = False
        while(True):
            if(not first_connected):
                msg = await ws.recv()
                print(msg)
                await ws.send("Hello! I am " + input("Enter your in-game name: "))
                msg = await ws.recv()
                while msg == "Name already in use, try a different name":
                    print(msg)
                    await ws.send("Hello! I am " + input("Enter your in-game name: "))
                    msg = await ws.recv()
                name = msg.split(" ")[1][0:-1]
                #print(name)
                first_connected = True
            userIn = input('Enter your target: ')
            await ws.send(userIn)
            msg = await ws.recv()
            if "You attacked " in msg:
                print(msg)
                msg = await ws.recv()
                if f'{name} got 0 votes' not in msg and f'{name} got 1 votes' not in msg:
                    print(msg)
                    print("You didn't get zero or 1 votes and were removed!")
                    ws.close()
                    return
                print(msg)
            else:
                print(msg)
             

get_ip()
# Start the connection
loop = asyncio.new_event_loop()
loop.run_until_complete(listen()) # loop until done