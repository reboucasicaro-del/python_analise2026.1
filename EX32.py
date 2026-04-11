# desenvolva um código python que leia 5 idades, diga se cada
# um é maior de idade, menor de idade ou idoso

for i in range(5):
    id = int(input("Digite a sua idade => "))
    if id < 18:
        print("menor de idade")
    elif id >= 65:
        print("idoso")
    else:
        print("maior de idade")
