from flask import jsonify,abort
from werkzeug.exceptions import HTTPException
from typing import Dict

code_to_message:Dict [int,str] = {
    500:"Sorry for the error, man. I'm trying my best.",
    400:"Not exactly the most 'well formed' of requests, huh?",
    404:"Unfortunately, I can't find that page. :<",
    401:"Nice try buddy. Try again with some authorization"
}

def init_errorHandler(myApp):     
    # error with message and code
    @ myApp.errorhandler(HTTPException)
    def error(e:HTTPException):
        message = {
            "error": e.name,   
            "details": code_to_message[e.code] if (e.code in code_to_message.keys()) else str(e)
        }
        return jsonify(message),e.code 
    
# error with code 
def throw(code:int):
    abort(code,code_to_message[code] if (code in code_to_message.keys()) else None)


