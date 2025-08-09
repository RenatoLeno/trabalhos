# Lista de produtos
class Produto:
    def __init__(self, nome, codigo, categoria, descricao, tempo_preparo, valor):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria
        self.descricao = descricao
        self.tempo_preparo = tempo_preparo
        self.valor = valor

    # Retorno dos dados
    def dicionario(self):
        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "tempo_preparo": self.tempo_preparo,
            "valor": self.valor
        }

# Lista dos produtos cadastrados
produtos = []

# Cadastro de um produto
def cadastrar_produto():
    print("\n Cadastro de Produto")
    
    nome = input("Nome do produto: ")
    codigo = input("Código: ")
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    
    try:
        tempo_preparo = int(input("Tempo de preparo (em minutos): "))
        valor = float(input("Valor (R$): "))
    except ValueError:
        print("Erro: Tempo deve ser número inteiro e valor deve ser número decimal.")
        return

    # Produto cadastrado
    novo_produto = Produto(nome, codigo, categoria, descricao, tempo_preparo, valor)
    
    # Confirmação do produto
    produtos.append(novo_produto.dicionario())
    print("Produto cadastrado com sucesso!")

# Função para exibir todos os produtos
def mostrar_produtos():
    print("\n Lista de Produtos Cadastrados")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for i, p in enumerate(produtos, start=1):
        print(f"\nProduto {i}:")
        print(f"  Nome: {p['nome']}")
        print(f"  Código de Barras: {p['codigo']}")
        print(f"  Categoria: {p['categoria']}")
        print(f"  Descrição: {p['descricao']}")
        print(f"  Tempo de Preparo: {p['tempo_preparo']} minutos")
        print(f"  Valor: R$ {p['valor']:.2f}")

# Exibição do menu
def main():
    while True:
        print("\n MENU ")
        print("1. Cadastrar produto")
        print("2. Mostrar produtos cadastrados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            mostrar_produtos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
main()
