from flask import Blueprint
from flask_socketio import emit
from middleware.validator import throw
from random import randint
from src.init import myApp,db,socketio
server_routes = Blueprint('server_routes', __name__)

#returns a list of all active websocket connections attached to the API
@server_routes.route('/get-all', methods=['GET'])
def get_servers():
    return {"message": "List of users"}

@server_routes.route('/connect/new', methods=['GET','POST'])
def create_room_ID():
    try: 
        roomID  = randint(1,9999) #generates a random ID room ID.TODO: overlap prevention
        port  = 9999
        db.set(roomID,port,ex=86400) #every room lasts for 24 hours (86400 seconds)
    except Exception: throw(500)

    return  {    
                "message": "Good Job, bud.",
                "serverID": roomID
            }

@server_routes.route('/connect/<path:roomID>', methods=['POST'])
def connect_to_websocket(roomID):
    create_web_socket(roomID)
    return {"message": "List of users"}

def create_web_socket(roomID:int):
    try:
        port:bytes = db.get(roomID) 
    except Exception:
        throw(500,"Something went wrong with the database connection.")
    if (not port): throw(404,"That room number is not valid bro.") 
    try:
        #creates the websocket
        socketio.run(myApp,host='0.0.0.0',port=int(port.decode()))
    except Exception:
        throw(500,"Something went wrong with socketIO.")
        
@socketio.on('message')
def handle_message(message):
    emit("Message recieved. Thanks for reaching out. Have a gold star.")

    # while True:
    #     client, addr = server.accept()      # accepts requests from the client.
    #     print(client.recv(1024).decode())   # prints it to the console 
    #     client.send("HELLLL YEAHHHHHHHHHHHHHHHh".encode())  # sends them a 'cool message' as a thank you.
