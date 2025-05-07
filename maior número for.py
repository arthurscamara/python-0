maior = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    
    while num < 0:
        print("Número inválido. Digite apenas números positivos.")
        num = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    
    if num > maior:
        maior = num

print(f"O maior número digitado foi: {maior}")
