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


def test_cria_produto():
    product = Product(*products)
    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.numero_de_serie, str)
    assert isinstance(product.instrucoes_de_armazenamento, str)
    assert product.id == 1
    assert product.nome_do_produto == "Nicotine Polacrilex"
    assert product.nome_da_empresa == "Target Corporation"
    assert product.data_de_fabricacao == "2021-02-18"
    assert product.data_de_validade == "2023-09-17" or ""
    assert product.instrucoes_de_armazenamento == "instrucao 1"
