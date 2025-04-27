produtos = [
    {"nome": "arroz", "preco": 10},
    {"nome": "feijao", "preco": 20}
]


carrinho = []

def adicionar_no_carrinho(produto):
    carrinho.append(produto)

def mostrar_produto():
    print("produtos disponiveis")
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto['nome'].capitalize()} - R${produto['preco']:.2f}")

mostrar_produto()

