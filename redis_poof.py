import redis
import json
redis_conection= redis.Redis(host="localhost",port=6379,db=0)
data_l = {
    'foo':'bar',
    'ans':42
}
#GUARDAR EN STRING
#redis_conection.set('commands','{"type":"voice_commands","payload":"oximeter"}')
dat = redis_conection.get('commands').decode(encoding='utf-8')
print(f"Estatus: {dat}")
print(f"")
print(f"Type: {type(dat)}")
print("JASON------")
dat2 = json.loads(dat)
print(f"Data json:{dat2} Type:{type(dat2)}")
print(f"------{dat2['payload']}")
dat3 = json.dumps(dat2)
print(f"Data json:{dat3} Type:{type(dat3)}")
#GUARDAR EN LISTAS
#redis_conection.rpush("voiceComands","oximeter")
#lo = redis_conection.lrange("voiceComands",0,-1)
#print(f"Correcto {type(lo)}")
#print(f"Ultimo elemento {type(lo[-1])}")
#print(f"Data:{lo[-1].decode(encoding='utf-8')}")
