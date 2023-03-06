from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if path.endswith(".csv"):
            with open(path, mode="r") as file:
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                list = [product for product in products]
                return list

        else:
            raise ValueError("Arquivo inválido")
