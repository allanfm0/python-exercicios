# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o seu salario.\nR$: "))
novo_salario = salario + (salario * 15 / 100)
print("O seu salario de R${}. com o aumento de 15% vai ser de: R$ {:.2f}.".format(salario, novo_salario))