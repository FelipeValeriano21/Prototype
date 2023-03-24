import copy 

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
    def clone(self):
        return copy.copy(self)
    
class PessoaManeger:
    def __init__(self):
      self.pessoas = {}

    def add_pessoa(self, nome, idade, id):
        pessoa = Pessoa(nome, idade)
        self.pessoas[id] = pessoa

    def get_pessoa(self, id):
       return self.pessoas[id].clone()
    
maneger = PessoaManeger();

maneger.add_pessoa("João", 30, 1)  
maneger.add_pessoa("Maria", 25, 2)   

Pessoa1 = maneger.get_pessoa(1)

Pessoa1.nome = "Felipe"

Pessoa2 = maneger.get_pessoa(1)

print(maneger.get_pessoa(1))
print(maneger.get_pessoa(2))
print(Pessoa2)

Pessoa2.nome = input("Digite seu novo nome")

print(Pessoa2)