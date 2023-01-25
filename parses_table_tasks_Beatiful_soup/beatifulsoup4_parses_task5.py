from constants import TABLE_TASK5
from parses_table_tasks_Beatiful_soup.base_class import BaseClass


class Table(BaseClass):
    def searching_green_elements_in_the_table(self, link):
        elements = [
            float(find_element.text)
            for find_element in self.send_requst_and_reply(link).find_all(
                "td", class_="green"
            )
        ]
        return elements

    def sum_elements(self, link):
        sum_all_elements = sum(self.searching_green_elements_in_the_table(link))
        return sum_all_elements


a = Table()
print(a.sum_elements(TABLE_TASK5))
