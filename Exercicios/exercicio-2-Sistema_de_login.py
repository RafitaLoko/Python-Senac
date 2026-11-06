print("--- Sistema de Login ---")

EMAIL_CADASTRADO = "admin@email.com"
SENHA_CADASTRADO = "1234"

email = input("Insira seu Email aqui: ")
senha = input("Insira sua senha aqui: ")


if email == EMAIL_CADASTRADO and senha == SENHA_CADASTRADO:
    print("Login realizado com sucesso!")
else:
    print("Não foi possivel realizar o login", "/ Algum dos dados está incorreto")

