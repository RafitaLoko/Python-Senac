from usuario import Usuario

class Usuario():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return(f"O nome do objeto usuario é {self.nome}")

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")



