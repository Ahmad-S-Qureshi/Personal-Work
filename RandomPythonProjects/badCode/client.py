import websockets
import asyncio
import sys
import os

sys.stderr = open(os.devnull, "w")


# The main function that will handle connection and communication 
# with the server

async def listen():
    global IP
    IP = input("Enter server IP: ")
    url = f"ws://{IP}:4206"
    # Connect to the server
    async with websockets.connect(url, ping_interval=None) as ws:
        # Send a greeting message
        connected = False
        while(True):
            if(not connected):
                msg = await ws.recv()
                print(msg)
                connected = True
                print("Welcome to the encryption game!")
                print("Player one will input a function (or a set of 2 functions)")
                print("The other players will then input numbers to test the function")
                print("This will continue until someone guesses the function or functions")
                print("Enjoy!")
            X = input("Enter value of your secret number or function (ex \"5\" or \"f(X) = X + 1, g(X) = X^2\"): ")
            X = X.replace("f(X)", "X")
            X = X.replace("g(X)", "X")
            X = X.replace(", ", "\n")
            print(X)
            
            try:
                (float)(X)
                await ws.send(X)
                msg = await ws.recv()
                print(msg)
                
            except:
                await ws.send(X)
                msg = await ws.recv()
                if "value of 3" in msg:
                    print(msg)
                    msg = await ws.recv()
                    print(msg)
                else:
                    print(msg)

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())