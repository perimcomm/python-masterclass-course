import redis
import logging
try:
    redis = redis.Redis(host='172.17.0.2', port=6379, db=0)
    logging.warn("Conexao realizada com sucesso")
except:
    logging.error("Erro ao realizar a conexao")



redis.smembers('circle:jdoe:soccer')

