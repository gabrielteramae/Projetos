produtos = [
    {"nome": "arroz", "preco": 10},
    {"nome": "feijao", "preco": 20}
]


carrinho = []

def adicionar_no_carrinho(produto):
    carrinho.append(produto)

adicionar_no_carrinho(produtos[0])

print(carrinho)

carrinho2 = []

def adicionar_no_carrinho_2(produto):
    carrinho2.append(produto)

adicionar_no_carrinho_2(produtos[1])

print(carrinho2)

