import websockets
import asyncio
import socket
import time
import sys
import os

#sys.stderr = open(os.devnull, "w")


# The main function that will handle connection and communication 
# with the server

async def listen():
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
                while msg == "Name already in use, try a different name":
                    print(msg)
                    await ws.send("Hello! I am " + input("Enter your in-game name: "))
                    msg = await ws.recv()
                name = msg.split(" ")[1][0:-1]
                msg = await ws.recv()
                print(msg)
                first_connected = True
            userIn = input('Enter "rock" "paper" or "scissors": ')
            await ws.send(userIn)
            msg = await ws.recv()
            if "Valid" in msg:
                print(msg)
                while(("Tie" not in msg) and ("wins!" not in msg)):
                    msg = await ws.recv()
                    print(msg)
            else:
                print(msg)
             

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())