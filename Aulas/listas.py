frutas = ["Maça", "Banana", "Mamão", "Uva"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Rafael", 20, True, "Estudante"]

for dado in dados:
    print(f"dado {dado}")

alunos = []

alunos.append("Guilherme")
alunos.append("Vitor")
alunos.append("Pedro")

print(f"alunos[0] {alunos[0]}")
print(f"alunos[1] {alunos[1]}")
print(f"alunos[2] {alunos[-1]}")

alunos[1] = "Ana"

print(alunos)

alunos.insert(1, "Gabriela")

print(alunos)

alunos.remove("Guilherme")

print(alunos)

#sem parametro, remove ultimo / com parametro, remove por indice
alunos.pop(1)

print(alunos)

tamanho_lista = len(alunos)

print(f"Tamanho lista {tamanho_lista}")