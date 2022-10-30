from statistics import mode
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, products):
        oldest_fabrication = min([x["data_de_fabricacao"] for x in products])
        nearest_expiration_date = min(
            [
                x["data_de_validade"]
                for x in products
                if x["data_de_validade"] > datetime.now().isoformat()
            ]
        )
        company_with_most_products = mode(
            [x["nome_da_empresa"] for x in products]
        )
        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
