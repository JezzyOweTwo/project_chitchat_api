from src.utils import throw
from typing import Dict, Any

def bodyValidator(requiredFields:list[str],body) -> Dict[str, Any]:  
    for field in requiredFields:
        if field not in body:
            throw(400,f"Your request is missing {field}!")
        
    return body

def headValidator(requiredFields:list[str],header):
    for field in requiredFields:
        if not header.get(field):
            throw(400,f"Your request is missing the header {field}!")
    return header 