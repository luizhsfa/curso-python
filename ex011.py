b = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))

area = b * a

# A cada 2m de parede, necessário 1litro de tinta

t = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta.'.format(b, a, area, t))