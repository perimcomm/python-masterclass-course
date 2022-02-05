import typing
from functools import lru_cache

class Pessoa:
    amarelo = "banana"

    @lru_cache
    def __init__(self, nome: str, sobrenome: str) -> object:
        self.nome = nome,
        self.ovo = sobrenome
    
    def get_fruta(self):
        return self.amareloamarelo
    
    
        

person = Pessoa(nome="bruno", sobrenome="laco")

print(person.get_fruta())
