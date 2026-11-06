print("Média escolar do aluno")


nome = input("Qual é o seu nome? ")
try:
    nota1 = float(input("Qual é a sua primeira nota? "))
    print(f"Sua primeira nota é {nota1}")

    nota2 = float(input("Qual é a sua segunda nota? "))
    print(f"Sua segunda nota é {nota2}")

    nota3 = float(input("Qual é a sua terceira nota? "))
    print(f"Sua terceira nota é {nota3}")

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print(f"Aluno {nome} está aprovado / Nota final {media:.2f}")
    elif 5 <= media <= 6.9:
        print(f"Aluno {nome} está em recuperação / Nota final {media:.2f}")
    else:
        print(f"aluno {nome} está reprovado / Nota final {media:.2f}")



except Exception:
    print("Insira um valor válido")
