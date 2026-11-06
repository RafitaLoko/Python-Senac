usuario = {
    "nome": "João",
    "email": "joao@email.com",
    "idade": 20,
    "ativo": True,
    "pets": ["junior, peixe"]
}

print(usuario)

print(f"nome: {usuario["nome"]}")
print(f"idade: {usuario["idade"]}")

usuario["idade"] = 25
usuario["cidade"] = "Santa Cruz do Sul"

print(f"nova idade {usuario["idade"]}")
print(f"cidade {usuario["cidade"]}")

del usuario["idade"]
pets = usuario.pop("pets")

print(usuario)

for chave, valor in ususario.items():
    print(f"chave: {chave} | valor: {valor}")

    