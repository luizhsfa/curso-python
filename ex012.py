#Primeiro solicite o valor do produto
preco = float(input('Qual é o preço do prduto? R$ '))
#Segundo determine o valor do desconto do produto
novo = preco - (preco * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, novo))