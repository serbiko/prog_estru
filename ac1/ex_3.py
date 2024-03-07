def determina_tipo_triangulo(l1, l2, l3):
    if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
        return "Não é triângulo"
    if l1 == l2 and l2 == l3:
        return "Equilatero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return "isosceles"
    else: 
        return "escaleno"



def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo


testa_triangulo()