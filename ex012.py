# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto.\nR$: "))
novo_preco = preco - (preco * 5 / 100)
print(f"O produto que custava R${preco}. Na promocao com 5% de desconto vai fica: R${novo_preco}")