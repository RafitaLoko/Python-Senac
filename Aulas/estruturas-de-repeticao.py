#contador = 1

# while contador <= 10:
    
#     if contador == 3:
#         contador += 1
#         continue

#     if contador == 7:
#         break

#     print(f"contador {contador}")
#     contador += 1
    


# print("Usando somente o numero final")
# for numero in range(5):
#     print(f"numero {numero}")


# print("")
# print("Usando numero inicial e numero final")
# for numero in range(1, 5):
#     print(f"numero {numero}")

# print("")
# print("Usando numero inicial, numero final e incremental")
# sequencia = range(0, 11, 2)
# for numero in sequencia:
#     print(f"numero {numero}")

# print("")
# print("Usando numero inicial, numero final e incremental - contador negativo")
# sequencia = range(10, -1, -1)
# for numero in sequencia:
#     print(f"numero {numero}")


for letra in "Rafael":
    print(f"letra {letra}")
    
frutas = ["Maça", "Banana", "Mamão"]

for fruta in frutas:
    print(f"fruta {fruta}") 

print("")
print("Usando enumerate")
for indice, fruta in enumerate(frutas):
    print(f"indice {indice}: {fruta}")

print("")
print("Usando enumerate e start")
for indice, fruta in enumerate(frutas, start=1):
    print(f"indice {indice}: {fruta}")