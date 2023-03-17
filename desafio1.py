"""
    OBTER SALÁRIO DO USUÁRIO E CALCULAR IMPOSTO DE RENDA
"""

# obter salário
salario = float(input("Digite seu salário: "))

alqIr1 = 0.075
alqIr2 = 0.15
alqIr3 = 0.225
alqIr4 = 0.275

# condições
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

salarioLiquido = salario - ir

# resultado
print(f"""
Sálario...........: R$ {salario:9.2f}
IR................: R$ {ir:9.2f}
Salário Líquido...: R$ {salarioLiquido:9.2f}
""")