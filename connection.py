'''
	Este codigo contiene el administrador de operaciones mediante comando de voz
'''
#import Tex_Spe  as TS
#import Spe_Text as ST
import subprocess
import os
import time
import json
#import ComandsQ
from redis import Redis 

r=Redis(host="localhost",port=6379)
while True:
    message=r.blpop("voiceEvents",0)
    if not message:
        continue
    
    print(message)
    data=json.loads(message[1])
    print(data)
    break
    '''if(Texto=="apagar"):
        r.rpush("voiceComands",'off')
     
    

    if(Texto=="hora"):
        os.system("python Hora.py")
        #r.set("voiceComand",'time')
        r.rpush("voiceComands","time")
      

    if "google" in Texto:
        #Consulta = Texto.replace("google","")
        r.rpush("voiceComands",'google')
        #print(Consulta)
        #os.system("python google.py "+Consulta)'''
        
    

	



