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





import json
#import ComandsQ
#Configuracion de redis
from redis import Redis
redis_connection = Redis(host="localhost",port=6379,db=0)	


def filter_command(request_redis):
	try:
		dict_request = json.loads(request_redis)
		return dict_request['payload']

	except Exception as ex_filter_command:
		print(f"Fail Filter Command {ex_filter_command}")

def status_oximeter():
	get_status_oximeter = redis_connection.get('status_oximeter').decode(encoding='utf-8')
	return get_status_oximeter


while True:
	#Ejecutar las consultas
	try:
		#redis_connection.set('commands','{"type":"voice_commands","payload":"oximeter"}')
		request_redis = redis_connection.get('commands').decode(encoding='utf-8')
		"""
		Description: reques_redist resive una consulta en formato de string de redis, que proviene de commands.
			commands={type:type_comand,payload:option}
			@type_command: str : [voice_commads,manual_commands ...]
			@payload: str : [oximeter,etc ...]
			@return: str: debera ser convertifo a json.
		"""
		#Obtener el comando seleccionado
		selected_command = filter_command(request_redis)
		#Filtrar los comandos
		if(selected_command == "oximeter"):
			print("Ejercutar oximetro")
			status = status_oximeter()
			print(status)
		else:
			print("Ejecutar otro")
		#print(f"Data: {request_redis}")



	except Exception as Ex:
		print(f"Fail consult redis : {Ex}")
		continue