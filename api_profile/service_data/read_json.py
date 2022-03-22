import json


class ReadJson(object):
    __instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(ReadJson, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.ip = None
        self.port = None
        self.mail = None
        self.password_for_email = None
        self.password = None
        self.first_name = None
        self.second_name = None

    def read_json(self):
        with open("api\\service_data\\configuration.json", "r") as read_file:
            data = json.load(read_file)
            self.ip = data["ip"]
            self.port = data["port"]
            self.mail = data["mail"]
            self.password_for_email = data["password_for_email"]
            self.password = data["password"]
            self.first_name = data["first_name"]
            self.second_name = data["second_name"]
