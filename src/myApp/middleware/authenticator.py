from myApp.utils import throw
from flask import request
from myApp.init import db
from middleware.validator import headValidator as validator
from datetime import datetime,timedelta
import jwt
import secrets
import os
from typing import Any,Dict

def userAuth(header) -> Dict[str, Any]:
    header = validator(["user-token"],header) # ensures the user passes their token in the header.
    user_token = header.get("user-token")     # gets user token from the header
               
    try:
        jwt.decode(user_token, os.getenv("JWT_KEY"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        throw(401,"Your time's up buddy. You'll need a new account now.")
    except jwt.InvalidTokenError: throw(401) # intentionally vague message. User auth messages should be as such. 
    except Exception: throw(500)

    try:
        user_data:bytes = db.get(user_token)
    except Exception:
        throw(500,"Sorry man. Something went wrong with the database connection.")
    if (not user_data): throw(401,"Your time's up buddy. You'll need a new account now.")
    return user_data.decode("utf-8")

def apiAuth():
    return 0    

# unique ID generator
def idGenerator(secureMode:bool=True):
    user_token = {"ip":request.host_url,"exp":datetime.now()+timedelta(seconds=86400)}   # sets the token to expire after 1 day
    if (secureMode):
        user_token.update   ({  "randNum":secrets.token_hex(16),
                                "curTime":datetime.now().strftime(format="%d/%m/%Y, %H:%M:%S"),
                                "lang":request.user_agent.language,
                                "platform":request.user_agent.platform,
                                "browser":request.user_agent.browser
                            })
    try:
        user_token = jwt.encode(user_token, os.getenv("JWT_KEY"), algorithm="HS256")
        db.set(user_token,"PP. HEHE",ex=86400)  # creates a key that lasts for 24 hours
        
    except Exception:
        throw(500)
    return user_token   