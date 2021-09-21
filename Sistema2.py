import subprocess
import os
import time
#import ComandsQ

#Configuracion de redis
from redis import Redis 
redis_conection =Redis(host="localhost",port=6379)

Encendido = True #Este es el estao de astro

#queue=ComandsQ.CreatQ()
Nombre = 'Astro'

#Inicia el protocolo para escuchar a diestra y siniestra
while (Encendido == True):

	#Instruccion para detectar el nombre del asistente
	#Llamado(Nombre)

	#Escuchamos la instruccion
	Duracion = 4 
	Spe_Text = ST.STT()
	print("\n\n Te escucho ........ \n\n")
	Texto = Spe_Text.Lisen(Duracion)
	print(Texto)


	Intentos = 0
	Success = False
    #hola como estas
	while(Intentos<3 and Success ==False):

		if(Texto=="apagar"):
			redis_conection .rpush("voiceComands",'off')
			Success = True
			Encendido=False

		if(Texto=="hora"):
			os.system("python Hora.py")
			#r.set("voiceComand",'time')
			redis_conection .rpush("voiceComands","time")
			Success = True

		if "google" in Texto:
			Consulta = Texto.replace("google","")
			redis_conection .rpush("voiceComands",'google')
			print(Consulta)
			os.system("python google.py "+Consulta)
			Success = True
#{type:"VoiceComand",payload:"Oximetro"}      
        if "Oximetro" in Texto:
            oximetro.connection(type:"VoiceComand",payload:"Oximetro")
            Success=True

		

            redis_conection .rpush
        Intentos +=1

class Oximetro(objeto):
    redis_auxiliar=[]
	def conection(self,comands):
		print("oximetro conectado")
    	redis_auxiliar.append(objeto)

		#Recuperar los datos del oximetro