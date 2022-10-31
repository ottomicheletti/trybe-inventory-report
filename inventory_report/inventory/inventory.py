import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if type == "simples":
            with open(path, "r") as file:
                inventory = csv.DictReader(file)
                return SimpleReport.generate(list(inventory))
        if type == "completo":
            with open(path, "r") as file:
                inventory = csv.DictReader(file)
                return CompleteReport.generate(list(inventory))
