from constants import TABLE_TASK7
from parses_table_tasks.base_class import BaseClass


class Table(BaseClass):
    def search_headers_columns(self, link):
        elements = [
            find_element.text
            for find_element in self.send_requst_and_reply(link).find("tr")
        ]
        elements_headers_columns = elements[1::2]
        elements_headers = {}
        for i in elements_headers_columns:
            elements_headers[i] = 0
        return elements_headers

    def elements_columns(self, link):
        elements_columns = []
        for i in range(1, 16):
            elements = [
                find_element.text.split("\n")[i]
                for find_element in self.send_requst_and_reply(link).find_all("tr")[1::]
            ]
            elements_columns.append(list(map(float, elements)))
        return elements_columns

    def find_sum_and_round(self, link):
        elements = []
        for i in self.elements_columns(link):
            elements.append(round(sum(i), 3))
        return elements

    def generate_dict_with_data(self, link):
        data = {}
        for current_column, current_sum in zip(
            self.search_headers_columns(link), self.find_sum_and_round(link)
        ):
            data[current_column] = current_sum
        return data


a = Table()
print(a.generate_dict_with_data(TABLE_TASK7))
