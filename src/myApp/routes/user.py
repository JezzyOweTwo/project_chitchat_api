from flask import Blueprint,request,jsonify
from myApp.middleware.validator import bodyValidator as validator
from myApp.middleware.authenticator import userAuth as auth
from myApp.middleware.authenticator import idGenerator
user_routes = Blueprint('user_routes', __name__)

# protected route returning all connections active websocket connections
@ user_routes.route('/get-connections', methods=['GET'])
def get_all_active_connections():
    # middleware function that checks userAuth
    return jsonify({"message": "I'm glad this works, but this route is NOT done yet, bro."}),500

# creates a unique key for the user, 
@ user_routes.route('/login/new', methods=['GET'])
def login_new_user():
    body = validator(["secure-mode"],request.get_json())
    isSecureMode = body.get("secure-mode")  
    user_token = idGenerator(isSecureMode)
    return jsonify({"message": "Lowkey, kinda suprised this works."},{"user-token":user_token}),200

# logs the user in 
@ user_routes.route('/login/', methods=['GET'])
def login():
    userData = auth(request.headers)
    return jsonify({"message": "Good job, mr.coder man."},{"user-data":userData}),200

# connects the user to a websocket the user in
@ user_routes.route('/connect/', methods=['POST'])
def connect():
    auth(request.headers) 
    return jsonify({"message": "I'm glad this works, but this route is NOT done yet, bro."}),500

# disconnects the user to a websocket
# protected route, deviceID passed as a parameter
@ user_routes.route('/disconnect', methods=['POST'])
def disconnect():
    return {}

# this helper method checks if the websocket is still behaving as intended.
def websocketManager(client):
    return True