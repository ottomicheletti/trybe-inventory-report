import os
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, filename):
        _, file_ext = os.path.splitext(filename)
        if file_ext == ".csv":
            with open(filename, "r") as file:
                products = csv.DictReader(file)
                return list(products)
        else:
            raise ValueError("Arquivo inválido")
