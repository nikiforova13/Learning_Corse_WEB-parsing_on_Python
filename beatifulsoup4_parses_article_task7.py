from base_class import BaseClass
from constants import TABLE_TASK7


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
        print("СЛоварь такой", elements_headers)
        return elements_headers

    def elements_columns(self, link):

        elements = [
            find_element.text.split("\n")
            for find_element in self.send_requst_and_reply(link).find_all("tr")[1::]
        ]
        print(elements)
        return elements

    def f(self, link):
        count = 0
        for current_element in self.elements_columns(link):
            print(current_element)
            for j in current_element:
                print(j)
                count += 1
                (self.search_headers_columns(link))[f"{count} column"] = j
                print("dsaaaaaaa", count)
                if count == 16:
                    count = 0


a = Table()
# print(a.search_headers_columns(TABLE_TASK7))
print(a.f(TABLE_TASK7))
