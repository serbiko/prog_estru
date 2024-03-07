def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a/b


def calculadora(n1, n2, opd):
    if type(opd) != int:
        return print("Operação inválida.")
    if opd == 1:
        print(soma(n1, n2))
    elif opd == 2:
        print(subtracao(n1, n2))
    elif opd == 3:
        print(multiplicacao(n1, n2))
    elif opd == 4:
        print(divisao(n1, n2))
    else:
        print("Operação inválida.")


calculadora(float(input("Informe o primeiro número:")), float(input("Insira o segundo número:")), input("1-soma\n2-Subtração\n3-Multipliação\n4-Divisão\nInsira o número da operação:"))

