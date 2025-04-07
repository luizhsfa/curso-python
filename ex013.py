salario = float(input('Qual é o salário do funcionário? R$'))
desconto = float(input('Qual a porcentagem de desconto: '))

novosalario = salario + (salario * desconto / 100)

print('Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}.'.format(salario, desconto, novosalario))