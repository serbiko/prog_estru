def bhaskara(a, b, c):
    r1 = (-(b) + ((b**2)-4*a*c)**0.5)/(2*a)
    r2 = (-(b) - ((b**2)-4*a*c)**0.5)/(2*a)
    print(r1)
    print(r2)


def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            print("Não é bissexto.")
        else:
            print("É bissexto.")
    else:
        print("Não é bissexto.")

