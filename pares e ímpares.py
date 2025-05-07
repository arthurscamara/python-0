# Programa que imprime os números pares de 100 a 1 (decrescente)

for numero in range(100, 0, -1):  
    if numero % 2 == 0:
        print(numero, end=" ")


# Programa que imprime os números ímpares de 100 a 1 (decrescente)

for numero in range(100, 0, -1):  
    if numero % 2 != 0:
        print(numero, end=" ")
