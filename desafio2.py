"""
    OBTER SALÁRIO DO USUÁRIO E CALCULAR IMPOSTO DE RENDA E O INSS

    SALARIO LIQUIDO = SALARIO - IR - INNS
"""

# obter salário
salario = float(input("Digite seu salário: "))

# condições

alqIr1 = 0.075
alqIr2 = 0.15
alqIr3 = 0.225
alqIr4 = 0.275

# IR
if salario >= 0 and salario <= 1903.98:
    ir = 0

elif salario > 1903.98 and salario <= 2826.65:
    ir = salario * alqIr1 - 142.80

elif salario > 2826.66 and salario <= 3751.05:
    ir = salario * alqIr2 - 354.80

elif salario > 3751.05 and salario <= 4664.68:
    ir = salario * alqIr3 - 636.13

else:
    ir = salario * alqIr4 - 869.36

# INSS

alqInss1 = 0.075
alqInss2 = 0.09
alqInss3 = 0.12
alqInss4 = 0.14
alqInss5 = 1051

if salario >= 0 and salario <= 1302:
    inss = salario * alqInss1

elif salario > 1302 and salario <= 2572.29:
    inss = salario * alqInss2

elif salario > 2571.29 and salario <= 3856.94:
    inss = salario * alqInss3

elif salario < 3856.94 and salario <= 7507.49:
    inss = salario * alqInss4

else:
    inss = salario - alqInss5

salarioLiquido = salario - ir - inss

# resultado
print(f"""
Sálario...........: R$ {salario:9.2f}
IR................: R$ {ir:9.2f}
INSS..............: R$ {inss:9.2f}
Salário Líquido...: R$ {salarioLiquido:9.2f}
""")