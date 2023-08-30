import websockets
import asyncio
import socket
import os
import sys
from random import randint

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
connected = []

# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")
    await websocket.send("Successfully connected!")
    # Store a copy of the connected client
    # Handle incoming messages
    global playerOneTurn
    try:
        async for message in websocket:
            if(message[0:6] == "Hello!"):
                tokens = message.split(" ")
                name = tokens[len(tokens) - 1]
                print(f"got hello message with name {name}")
                try:
                    search_for_player(connected, name)
                    await websocket.send("Name already in use, try a different name")
                except NameError as e:
                    connected.append([websocket, name, str(randint(400, 900)) +', '+str(randint(400,900))])
                    print(f"stored player {name}")
                    print("sending welcome message")
                    await websocket.send(f"Welcome {name}!")
            
            elif (message[0:3] == 'Pos'):
                positions = []
                for connection in connected:
                    position = []
                    for token in connection[2].strip()[1:-1].split(', '):
                        position.append((int)(token))
                    position.append(connection[0])
                    positions.append(position)

                
                    if connection[0] == websocket:
                        connection[2] = message[4:]
                for position in range(0, len(positions)):
                    for position2 in range(position+1, len(positions)):
                        print('comparing positions')
                        if abs(positions[position][0]-positions[position2][0]) <= 10 and abs(positions[position][1]-positions[position2][1])<=10 and position!=position2:
                            print('position match, removing one player')
                            if randint(0,1) == 1:
                                await positions[position][2].close()
                            else:
                                await positions[position2][2].close()

                print(positions)

                position_message = ''
                for connection in connected:
                    position_message += connection[2]
                await websocket.send(position_message)
                
        # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        for connection in connected:
            if connection[0] == websocket:
                connected.remove(connection)

# Start the server
IP = get_ip()
print("Making server at " + IP + ":" + (str)(PORT))
start_server = websockets.serve(echo, get_ip(), PORT)
asyncio.get_event_loop().run_until_complete(start_server)
with open("running.txt", "w") as handler:
    handler.write("true")
asyncio.get_event_loop().run_forever()
