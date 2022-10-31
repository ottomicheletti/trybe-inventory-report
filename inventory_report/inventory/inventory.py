import os
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


exts = {
    ".csv": [
        lambda file: csv.DictReader(file),
        lambda inventory: list(inventory),
    ],
    ".json": [lambda file: json.load(file), lambda inventory: inventory],
}


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        _, file_ext = os.path.splitext(path)
        if type == "simples":
            with open(path, "r") as file:
                inventory = exts[file_ext][0](file)
                return SimpleReport.generate(exts[file_ext][1](inventory))
        if type == "completo":
            with open(path, "r") as file:
                inventory = exts[file_ext][0](file)
                return CompleteReport.generate(exts[file_ext][1](inventory))
