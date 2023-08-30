import websockets
import asyncio
import pygame
import pygame_textinput
from threading import Thread
import sys
from time import sleep
from random import randint

#sys.stderr = open(os.devnull, "w")

# The main function that will handle connection and communication 
# with the server
def pygame_init(elements, message):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    elements['screen'] = screen
    elements['player_coord'] = [randint(10, 90)*10, randint(10, 65)*10]

def pygame_update(elements, msg):
    elements['screen'].fill("purple")
    if msg != None:
        msg += ' '
        for token in msg.split('['):
            position_msg = token[:-2]
            position = []
            for token in position_msg.split(','):
                try:
                    position.append(int(token.strip().strip().strip()))
                except:
                    pass
                    #print(token.strip())
            #try:
            print(len(position))
            if len(position) == 2:
                pygame.draw.circle(elements['screen'], "red", position, 40)
            #except:
                #pass
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # fill the screen with a color to wipe away anything from last frame
    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        elements['player_coord'][1] -= 10
    if keys[pygame.K_s]:
        elements['player_coord'][1] += 10
    if keys[pygame.K_a]:
        elements['player_coord'][0] -= 10
    if keys[pygame.K_d]:
        elements['player_coord'][0] += 10

    # flip() the display to put your work on screen
    pygame.display.flip()



async def listen():
    pygame_elements = {}
    IP = input("Enter server IP: ")
    url = f"ws://{IP}:4206"
    # Connect to the server
    async with websockets.connect(url, ping_interval = 1) as ws:
        # Send a greeting message
        first_connected = False
        
        while(True):
            if(not first_connected):
                await ws.send("Hello! I am " + input("Enter your in-game name: "))
                msg = await ws.recv()
                if('Success' not in msg):
                    print("connection failed")
                msg = await ws.recv()
                while "Name already in use" in msg:
                    print(msg)
                    await ws.send("Hello! I am " + input("Enter your in-game name: "))
                    msg = await ws.recv()
                name = msg.split(" ")[1][0:-1]
                pygame_init(pygame_elements, [])
                print(msg)
                first_connected = True
            try:
                msg= await asyncio.wait_for(ws.recv(), timeout=0.1)
            except:
                msg = None
            await ws.send("Pos: " + str(pygame_elements['player_coord']))
            sleep(0.1)
            pygame_update(pygame_elements, msg)

            

             

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())