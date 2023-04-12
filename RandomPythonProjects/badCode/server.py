import websockets
import asyncio
import socket
import os
import sys

sys.stderr = open(os.devnull, "w")

def get_val_with_function(val, function):

    with open("codeIn.py", "w") as handler:
        print(val)
        handler.write("X = "+ (val) +"\n" +
        function + "\n" 
        "with open(\"codeOut.txt\", \"w\") as handler:" + "\n"
            "\t""handler.write((str)(X))")
    os.system("python3 codeIn.py")
    




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

# Server data
PORT = (int)(4206.9)
print("Server listening on Port " + str(PORT))

# A set of connected ws clients
connected = set()
connector_with_function = None

# The main behavior function for this server
global function_string
function_string = None



async def echo(websocket, path):
    print("A client just connected")
    await websocket.send("Successfully connected!")
    # Store a copy of the connected client
    connected.add(websocket)
    # Handle incoming messages
    try:
        global function_string
        async for message in websocket:
            try:
                X = (float)(message)
                if(function_string == None):
                    await websocket.send("Function not inputted yet!")
                else:
                    get_val_with_function(message, function_string)
                    with open("codeOut.txt", "r") as handler:
                        await websocket.send("Your value in the function is " + handler.read())

            except:
                if function_string == None:
                    function_string = message
                    get_val_with_function("3", function_string)
                    with open("codeOut.txt", "r") as handler:
                        await websocket.send("The value of 3 with your function is " + handler.read())
                    print(function_string)
                
                elif function_string == message:
                    for conn in connected:
                        await conn.send("Someone guesssed the function, set the next one!")
                        function_string = None

                else:
                    await websocket.send("Oops, wrong guess of the function!")
                    
    # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

# Start the server
IP = get_ip()
print("Making server at " + IP + ":" + (str)(PORT))
start_server = websockets.serve(echo, get_ip(), PORT, ping_interval = None)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
