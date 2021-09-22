import time
import json
#import ComandsQ
from redis import Redis 

r=Redis(host="localhost",port=6379)

def apagar():
    print("apagar")

def get_Time():
    print("time")
    
while True:
    message=r.blpop("voiceEvents",0)
    if not message:
        continue
    
    data=json.loads(message[1])
    print(data)
    
    if data["type"]== "voiceComands":
        payload=data["payload"]
    
        if payload=="apagar":
          apagar()
                  
        elif payload=="time":
            get_Time()

        elif "google" in payload:
            print("google")
    #break
