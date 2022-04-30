from framework.base_element import BaseElement


class String(BaseElement):
    def get_text(self):
        element = self.find_element_by_xpath()
        return element.text
    