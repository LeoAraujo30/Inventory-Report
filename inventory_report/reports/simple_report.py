from datetime import date


class SimpleReport:
    @classmethod
    def __get_fabrication_date(cls, list):
        fabrication = list[0]["data_de_fabricacao"]
        for dict in list:
            new_fabrication = date.fromisoformat(dict["data_de_fabricacao"])
            if new_fabrication < date.fromisoformat(fabrication):
                fabrication = dict["data_de_fabricacao"]

        return fabrication

    @classmethod
    def __get_validate_date(cls, list):
        dates = []
        for dict in list:
            if date.fromisoformat(dict["data_de_validade"]) >= date.today():
                dates.append(dict["data_de_validade"])

        validate = dates[0]
        for string_date in dates:
            new_validate = date.fromisoformat(string_date)
            if new_validate < date.fromisoformat(validate):
                validate = string_date

        return validate

    @classmethod
    def _get_names(cls, list):
        names = []
        for dict in list:
            if dict["nome_da_empresa"] not in names:
                names.append(dict["nome_da_empresa"])

        return names

    @classmethod
    def _get_quantity(cls, names, list):
        quantity = []
        for name in names:
            number = 0
            for dict in list:
                if dict["nome_da_empresa"] == name:
                    number += 1

            quantity.append(number)

        return quantity

    @classmethod
    def generate(cls, list):
        names = cls._get_names(list)
        quantity = cls._get_quantity(names, list)
        index = quantity.index(max(quantity))

        return (
            "Data de fabricação mais antiga: "
            f"{cls.__get_fabrication_date(list)}\n"
            "Data de validade mais próxima: "
            f"{cls.__get_validate_date(list)}\n"
            "Empresa com mais produtos: "
            f"{names[index]}"
        )
