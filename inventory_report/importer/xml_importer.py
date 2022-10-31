import os
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filename):
        _, file_ext = os.path.splitext(filename)
        if file_ext == ".xml":
            with open(filename, "r") as file:
                products = xmltodict.parse(file.read())["dataset"]["record"]
                return list(products)
        else:
            raise ValueError("Arquivo inválido")
