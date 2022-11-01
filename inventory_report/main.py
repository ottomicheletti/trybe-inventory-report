import os
import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    file_importers = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }
    _, file_ext = os.path.splitext(sys.argv[1])

    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        report = InventoryRefactor(file_importers[file_ext]).import_data(
            sys.argv[1], sys.argv[2]
        )
        sys.stdout.write(report)
