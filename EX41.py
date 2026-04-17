# desenvolva um código python usando while que digite um nome
# e imprima, só pare o programa ao digitar sair
# != diferente
# break
nome = ""
while nome != "sair":
    nome = input("Digite um nome => ").lower()
    if nome == "sair":
        break # o break só funciona com if
    print(f"Olá {nome}")
