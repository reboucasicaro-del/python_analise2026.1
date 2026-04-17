# desenvolva um código python que envie um valor para uma função que
# essa verifique se o numero é impar ou par
def par_ou_impar(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "Impar"
numero = int(input("Digite um valor => "))
resultado = par_ou_impar(numero)
print(resultado)
