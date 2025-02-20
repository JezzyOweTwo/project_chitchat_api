from redis import Redis
from flask_socketio import SocketIO
import os
from flask import Flask,Blueprint
from typing import Dict
# from routes.server import server_routes
# from routes.user import user_routes
from utils import throw
from flask import jsonify
from werkzeug.exceptions import HTTPException
import logging
from dotenv import load_dotenv

def init_database() -> Redis: 
   return Redis(os.getenv("SERVER_URL"),os.getenv("SERVER_PORT"))

def init_routes(routes:Dict[str,Blueprint],myApp)-> None:
    # middleware to pass all 'server' requests to server route
    for route in routes.keys():
        myApp.register_blueprint(routes.get(route), url_prefix=route)
        
    # if neither of the middlewares of activated, the route could not be located
    @myApp.route('/<path:path>', methods=['GET', 'POST','PUT','DELETE'])
    @myApp.route('/', methods=['GET', 'POST','PUT','DELETE'])
    def not_found(path): throw(404)

def init_socketIO(myApp) -> SocketIO:
    return SocketIO(myApp)

def init_flask() -> Flask:
    return Flask(__name__) #intantiates the Flask server

def init_errorHandler(myApp):
    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
     
    # error with message and code
    @ myApp.errorhandler(HTTPException)
    def error(e:HTTPException):
        logging.error("ERROR", exc_info=True)  # Logs the full traceback
        message = {
            "error": e.name,   
            "details": str(e)
        }
        return jsonify(message),e.code
    
load_dotenv()                   #loads the env
myApp =  init_flask()           # inits the app
socketio = init_socketIO(myApp) # inits socketIO
init_errorHandler(myApp)        # inits errorHandler
db = init_database()            # inits redis