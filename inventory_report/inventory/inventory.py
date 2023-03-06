from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def __get_data(cls, path: str):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)

        elif path.endswith(".json"):
            return JsonImporter.import_data(path)

        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)

    @classmethod
    def import_data(cls, path: str, string: str):
        if string == "simples":
            return SimpleReport.generate(cls.__get_data(path))

        if string == "completo":
            return CompleteReport.generate(cls.__get_data(path))
