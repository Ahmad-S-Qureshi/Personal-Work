import websockets
import asyncio
import socket
import os
import sys

sys.stderr = open(os.devnull, "w")

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

global playerOneTurn
playerOneTurn = None

global moves_completed
moves_completed = 0

# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")
    await websocket.send("Successfully connected!")
    # Handle incoming messages
    global moves_completed
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
                    connected.append([websocket, name, 0])
                    print(f"stored player {name}")
                    print("sending welcome message")
                    await websocket.send(f"Welcome {name}!")
            else:
                try:
                    target = search_for_player(connected, message)
                    for player in connected:
                        if player == target:
                            player[2]+=1
                            await websocket.send("You attacked " + target[1])
                            moves_completed+=1
                    if moves_completed > len(connected) - 1:
                        print("all moves submitted")
                        text = ""
                        for player in connected:
                            text += f"{player[1]} got {player[2]} votes\n"
                        text+="Removing players with one vote"
                        for player in connected:
                            await player[0].send(text)
                        for player in connected:
                            print(f"Player {player[1]} got {player[2]} votes")
                            if player[2] == 1:
                                await player[0].close()
                                print(f"removing {player[1]}")
                                connected.remove(player)
                            else:
                                print(player[1] + " was not removed")
                                player[2] == 0
                        moves_completed = 0
                except NameError as e:
                    await websocket.send((str)(e))
                
                
        # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        for conn in connected:
            if(conn[2] == name):
                connected.remove(conn)
    finally:
        pass
        #connected.remove(websocket)

# Start the server
IP = get_ip()
print("Making server at " + IP + ":" + (str)(PORT))
start_server = websockets.serve(echo, get_ip(), PORT)
asyncio.get_event_loop().run_until_complete(start_server)
with open("running.txt", "w") as handler:
    handler.write("true")
asyncio.get_event_loop().run_forever()
