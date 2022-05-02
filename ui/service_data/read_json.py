import json


class ReadJson(object):
    __instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(ReadJson, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.wait_time = None
        self.browser = []
        self.name_browser = None
        self.url = ""
        self.name_local = None
        self.username = None
        self.password = None
        self.code = None

    def read_json(self):
        with open("ui\\service_data\\configuration.json", "r") as read_file:
            data = json.load(read_file)
            self.browser = data["browser"]
            self.wait_time = data["wait_time"]
            self.name_browser = data["name_browser"]
            self.name_local = data["name_local"]
            self.url = data["url"]
            self.username = data["username"]
            self.password = data["password"]
            self.code = data["code"]
