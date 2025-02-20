from flask import abort
from typing import Dict

code_to_message:Dict [int,str] = {
    500:"Sorry for the error, man. I'm trying my best.",
    400:"Not exactly the most 'well formed' of requests, huh?",
    404:"Unfortunately, I can't find that page. :<",
    401:"Nice try buddy. Try again with some authorization"
}
    
# error with code 
def throw(code:int, message:str=None):
    if (message): abort(code,message)
    elif ( (not message) and (code in code_to_message.keys()) ): abort(code,code_to_message[code])
    else: abort(code)

