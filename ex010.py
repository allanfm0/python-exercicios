# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Dolar: R$ 4,92
# Euro: R$ 5,34
real = float(input("Quanto de dinheiro voce tem na carteira.\nR$: "))
dolar  = real / 4.92
euro = real / 5.34
print("Com R$ {} reais, voce pode comprar US$  {:.2f} dolares.".format(real, dolar))
print("Com R$ {} reais, voce pode comprar EUR$ {:.2f} euros.".format(real, euro))
