#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Kms foram percorridos? '))
dia = float(input('Quantos dias o carro ficou alugado? '))

valor = km * 0.15 + dia * 60

print('O total a pagar é de R${:.2f}'.format(valor))

