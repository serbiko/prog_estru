def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario = valor_hora * num_horas
    salario_final = salario - salario*irpf
    print("O salário é R$%0.2f." % salario_final)

calcula_salario(10, 100)