v1 = float(input("Valor original => "))
if v1 < 100:
    p = v1 * (5/100)
    d = v1 - p
elif v1 <= 499:
    p = v1 * (15/100)
    d = v1 - p
else:
    p = v1 * (20/100)
    d = v1 - p

print(f"Valor de {v1} com desconto {p} ficará em {d}")