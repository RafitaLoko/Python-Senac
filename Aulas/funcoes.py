# def saudacao():
#     print(f"Olá, mundo")

# saudacao()

# def saudacao_com_nome(nome="Aluno"):
#     print(f"Olá, meu nome é {nome}")

# saudacao_com_nome("caneta azul")
# saudacao_com_nome("Manoel gomes")
# saudacao_com_nome()


# def somar(a, b):
#     soma = a + b
#     return soma

# print(somar(5, 2))


def cadastrar_usuario(nome: str, idade: int = 18):
    print(f"Cadastrando nome {nome}")
    print(f"Cadastrando idade {idade}")


cadastrar_usuario("Manoel Gomes", 81)
cadastrar_usuario("João")

cadastrar_usuario(nome = "Douglas", idade = 32)
cadastrar_usuario(idade = 40, nome = "Eloi")
# cadastrar_usuario(idade = 40, "Marlene") dá erro
cadastrar_usuario("Marlene", idade = 48)
cadastrar_usuario(10, "Texto")

