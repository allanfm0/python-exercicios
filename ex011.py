# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input("altura da parede: "))
largura = float(input("largura da parede: "))
area = altura * largura

print(f"Sua parede tem a dimensão de {altura}x{largura} e sua area é de {area}m².")
tinta = area / 2
print(f"Para pintar a parede voce precisara de {tinta} litros de tinta.")