produto = float(input("Digite o preço original do produto:"))
print(produto)

porcentagem = float(input("Digite o valor da porcentagem do desconto:"))
print(porcentagem)

soma = porcentagem = produto * (porcentagem / 100)
print(soma)

preco_final = produto - porcentagem
print(preco_final)

print('valor do desconto:', porcentagem)
print('O preço final do produto', preco_final)
