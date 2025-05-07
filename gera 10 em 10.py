# Programa que gera a série: 10, 20, 30, ..., 1000 usando for

for numero in range(10, 1001, 10):
    print(numero, end=", " if numero < 1000 else "\n")
