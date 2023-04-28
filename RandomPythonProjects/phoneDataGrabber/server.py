import websockets
import asyncio
import socket
import os
import sys

#sys.stderr = open(os.devnull, "w")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def search_for_player(list_connected, player_target):
    for player in list_connected:
        if player[1]==player_target:
            return player
    raise NameError("Player not found")

# Server data
PORT = (int)(4206.9)
print("Server listening on Port " + str(PORT))


# A set of connected ws clients
connected = set()


# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")
    #await websocket.send("Successfully connected!")
    # Store a copy of the connected client
    # Handle incoming messages
    try:
        async for message in websocket:
            print(message)
        # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

# Start the server
IP = get_ip()
print("Making server at " + IP + ":" + (str)(PORT))
start_server = websockets.serve(echo, get_ip(), PORT)
asyncio.get_event_loop().run_until_complete(start_server)
with open("running.txt", "w") as handler:
    handler.write("true")
asyncio.get_event_loop().run_forever()
