from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if path.endswith(".json"):
            with open(path, mode="r") as file:
                list = json.load(file)
                return list

        else:
            raise ValueError("Arquivo inválido")
