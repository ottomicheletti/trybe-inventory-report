from inventory_report.inventory.product import Product

products = (
    1,
    "Nicotine Polacrilex",
    "Target Corporation",
    "2021-02-18",
    "2023-09-17",
    "CR25 1551 4467 2549 4402 1",
    "instrucao 1",
)


def test_relatorio_produto():
    product = Product(*products)
    assert repr(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
