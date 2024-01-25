# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'Numero: {num}')
print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print('Raiz quadrada: {:.2f}'.format(raiz))