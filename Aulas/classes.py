from usuario import Usuario


# class Usuario():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __str__(self):
#         return(f"O nome do objeto usuario é {self.nome}")

#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")


print("Execução normal do arquivo...")
usuario = Usuario("Rafael", 20) 
usuario2 = Usuario("Rogerio", 41)

print(f"objeto usuario {usuario}")

print(usuario.nome)
print(usuario.idade)

usuario.idade = 18

print(f"Nova idade do usuario: {usuario.idade}")
usuario.apresentar()
usuario2.apresentar()