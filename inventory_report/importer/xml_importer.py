from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if path.endswith(".xml"):
            list = []
            with open(path, mode="r") as file:
                dataset = ET.parse(file).getroot()
                for record in dataset:
                    list.append({
                        f"{record[0].tag}": record[0].text,
                        f"{record[1].tag}": record[1].text,
                        f"{record[2].tag}": record[2].text,
                        f"{record[3].tag}": record[3].text,
                        f"{record[4].tag}": record[4].text,
                        f"{record[5].tag}": record[5].text,
                        f"{record[6].tag}": record[6].text
                    })

                return list

        else:
            raise ValueError("Arquivo inválido")
