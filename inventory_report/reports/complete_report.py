from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, products):
        simple_report = SimpleReport.generate(products)
        industries = dict()
        for ind in products:
            if ind["nome_da_empresa"] in industries:
                industries[ind["nome_da_empresa"]] += 1
            else:
                industries[ind["nome_da_empresa"]] = 1
        industries_report = "".join(
            f"- {ind}: {qty}\n" for ind, qty in industries.items()
        )
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{industries_report}"
        )
