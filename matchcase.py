num1 = int(input('Digite um número:'))
print (num1)
operacao = input("Digite a operação(+,-,*,/): ")
num2 = int(input('Digite um número:'))
print (num2)
resultado = 0 

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado da soma: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado da subtrção: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")          



