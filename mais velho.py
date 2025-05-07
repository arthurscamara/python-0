
contador = 1
mais_velho_nome = ""
mais_velho_idade = 0
mais_velho_sexo = ""

while contador <= 5:
    print(f"\n--- Aluno {contador} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ")

    if idade > mais_velho_idade:
        mais_velho_idade = idade
        mais_velho_nome = nome
        mais_velho_sexo = sexo

    contador += 1

print("\n=== Aluno Mais Velho ===")
print(f"Nome: {mais_velho_nome}")
print(f"Idade: {mais_velho_idade}")
print(f"Sexo: {mais_velho_sexo}")
