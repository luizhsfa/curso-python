import math

a = float(input('Digite o ângulo que você deseja: '))

b = math.radians(a)

se = math.sin(b)
co = math.cos(b)
ta = math.tan(b)

print('O ângulo de {} tem o SENO de {:.2f}'.format(a, se))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, ta))