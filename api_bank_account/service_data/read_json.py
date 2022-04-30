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
        self.token = None
        self.user_id = None

    def read_json(self):
        with open("api_bank_account\\service_data\\configuration.json", "r") as read_file:
            data = json.load(read_file)
            self.ip = data["ip"]
            self.port = data["port"]
