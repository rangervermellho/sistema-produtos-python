import json

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def mostrar(self):
        print(f"Nome: {self.nome} | Valor: R$ {self.valor:.2f}")

    def to_dict(self):
        return {"nome": self.nome, "valor": self.valor}
    
    @staticmethod
    def from_dict(dados):
        return Produto(dados["nome"], dados["valor"])
