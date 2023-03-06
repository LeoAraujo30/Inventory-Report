import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def dict():
    return {
        "id": 1,
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    }


def test_cria_produto(dict):
    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1"
    )

    assert product.id == dict["id"]
    assert product.nome_do_produto == dict["nome_do_produto"]
    assert product.nome_da_empresa == dict["nome_da_empresa"]
    assert product.data_de_fabricacao == dict["data_de_fabricacao"]
    assert product.data_de_validade == dict["data_de_validade"]
    assert product.numero_de_serie == dict["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == dict[
        "instrucoes_de_armazenamento"
    ]
