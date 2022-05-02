from framework.base_element import BaseElement


class Filed(BaseElement):
    def input_data(self, data):
        self.send_key(data)
