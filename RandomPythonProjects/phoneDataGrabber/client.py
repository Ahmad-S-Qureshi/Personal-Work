import websockets
import asyncio
import sys
import os

sys.stderr = open(os.devnull, "w")


# The main function that will handle connection and communication 
# with the server

async def listen():
    IP = input("Enter server IP: ")
    url = f"ws://{IP}:4206"
    # Connect to the server
    async with websockets.connect(url, ping_interval = 1) as ws:
        while(True):
            msg = await ws.recv()
            print(msg)
            
             
# Start the connection
asyncio.get_event_loop().run_until_complete(listen())