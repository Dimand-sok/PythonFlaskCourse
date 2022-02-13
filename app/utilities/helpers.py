import re

def sanitize_key(key):
    return re.sub(r"\W","_").lower()
     