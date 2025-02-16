from flask import Blueprint,request,jsonify
from routes.errors import throw
user_routes = Blueprint('user_routes', __name__)

# protected route returning all connections active websocket connections
@ user_routes.route('/get_connections', methods=['GET'])
def get_all_active_connections():
    return jsonify({"message": "I'm glad this works, but this route is NOT done yet, bro."}),500

# connects the user to a websocket
# deviceID passed as a parameter
@ user_routes.route('/connect/', methods=['POST'])
def connect_user():
    try: body = request.get_json()
    except Exception: throw(400)
    if not "userID" in body: throw(400)
     
    return jsonify({"message": "I'm glad this works, but this route is NOT done yet, bro."}),500

# disconnects the user to a websocket
# protected route, deviceID passed as a parameter
@ user_routes.route('/disconnect', methods=['POST'])
def disconnect_user():
    return {}

# this helper method checks if the websocket is still behaving as intended.
def websocketManager(client):
    return True
