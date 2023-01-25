from base_class import BaseClass

from constants import TABLE_TASK2


class Table(BaseClass):
    def searching_elements_in_the_table(self, link):
        elements = [
            find_element.text
            for find_element in self.send_requst_and_reply(link).find_all("b")
        ]
        return elements

    def finding_the_sum_of_elements(self, link):
        sum_elements = 0
        for current_element in self.searching_elements_in_the_table(link):
            sum_elements += float(current_element)
        return sum_elements


a = Table()
print(a.finding_the_sum_of_elements(TABLE_TASK2))
