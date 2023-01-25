from base_class import BaseClass

from constants import TABLE_TASK3


class Table(BaseClass):
    def search_tr_td(self, link):
        elements = [i.text for i in self.send_requst_and_reply(link).find_all("td")]
        return set(elements)

    def sum_tr_td(self, link):
        sum = 0
        for i in self.search_tr_td(link):
            sum += float(i)
        return sum


a = Table()
print(a.sum_tr_td(TABLE_TASK3))
