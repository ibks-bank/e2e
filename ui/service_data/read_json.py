import json


class ReadJson(object):
    __instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ReadJson, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.browser = []

    def read_json(self):
        with open("ui\\service_data\\configuration.json", "r") as read_file:
            data = json.load(read_file)
            self.browser = data["browser"]
            self.wait_time = data["wait_time"]
