from flask import Blueprint
from myApp.middleware.validator import throw
from random import randint
from myApp.init import db
import os
import ssl
import threading

server_routes = Blueprint('server_routes', __name__)
active_rooms:dict[int,int] = {}   # map storing active room numbers corresponding ports

MAX_ROOMS = 10  # maximum number of chat rooms supported by one instance of the API
MAX_CONNECTIONS = 10 # maximum number of connections per chat room
## -------------------------------------------List Routes ------------------------------------------------##
# returns a list of all active websocket connections
@server_routes.route('/list/all/', methods=['GET'])
def show_global_rooms():
    try:
        all_rooms_bytes = db.keys("*")
        all_rooms  = [e.decode() for e in all_rooms_bytes]
    except Exception:
        throw(500,"Idk man. Blame Redis or somethin man.")
    if not all_rooms: return {"rooms":"not a single room is active rn."}
    return {"message": all_rooms}

#returns a list of all active websocket connections attached to the API
@server_routes.route('/list/local/', methods=['GET'])
def show_local_rooms():
    if not active_rooms: return {"rooms":"not a single room is active rn."}
    return {"rooms":active_rooms}

## -------------------------------------------Connect Routes ------------------------------------------------##
# @server_routes.route('/connect/<path:roomID>', methods=['GET'])
# def get_port(roomID):
#     print(active_rooms)
#     try:
#         port = active_rooms.get(int(roomID))
#     except Exception:
#         throw(400,"This stupid idiot is trying to connect to a non-numerical room code...")
#     if not port:
#         throw (404,"try again with a valid room ID man. :/")
#     return {"port":port}

@server_routes.route('/connect/new', methods=['GET','POST'])
def create_room_ID():
    try: 
        # id generation and port generation
        roomID  = randint(1,9999) # generates a random ID room ID.TODO: overlap prevention
        port  = randint(1,9999)
        db.set(roomID,port,ex=86400) # every room lasts for 24 hours (86400 seconds)

        # creates a new thread for this room
        server_thread = threading.Thread(target=create_room, args=(roomID,))
        server_thread.daemon = True  # Allows for parralel execiution
        server_thread.start() #starts the thread for the new room

        # active_rooms HashMap updated
        global active_rooms
        active_rooms[roomID] = port #<roomID,port> added to the active room HashMap 
    
    except Exception: throw(500)
    return  {    
                "message": "Good Job, bud.",
                "serverID": roomID,
                "port":port
            }
## --------------------------------------- Helper Methods  --------------------------------------- ##
def create_room(roomID:int): 
    try:
        port_bytes:bytes = db.get(roomID)
        host = os.getenv("WEBSOCKET_ADDRESS")
        
    except Exception:
        throw(500,"Something went wrong with the database connection.")
    if (not port_bytes): throw(404,"That room number is not valid bro.") 
    
    try:
        port=int( port_bytes.decode())  
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(MAX_CONNECTIONS)
        print(f"Server {host} started on port {port}")
    except Exception:
        throw(500,"Something went wrong when trying to instantiate the websocket. Smh.")
    
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        # Handle each client connection in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.daemon = True
        client_handler.start()

def handle_client(client):
    print("lets handle dat client, lol")
    client.send("Wow. That's wonderful. Genuinely suprised this shit works.".encode())
    client.close()