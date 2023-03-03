from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        names = SimpleReport._get_names(list)
        quantity = SimpleReport._get_quantity(names, list)
        index = 0
        string = ''

        while index < len(names):
            string += f"- {names[index]}: {quantity[index]}\n"
            index += 1

        return (
            f"{SimpleReport.generate(list)}\n"
            "Produtos estocados por empresa:\n"
            f"{string}"
        )
