import json


class JsonFileManager():
    def __init__(self, jsonFileName) -> None:
        with open(jsonFileName, "rb+") as f:
            file = f.read()
            self.json = json.loads(file)

    def readConfigFile(self, key):
        pass

    def writeConfigFile(self, key, value):
        pass


class ConfigManager(JsonFileManager):
    def __init__(self, jsonFileName) -> None:
        super(ConfigManager, self).__init__(jsonFileName)

        self.serverConfig = self.json['ServerConfig']


class ServerConfig(ConfigManager):
    def __init__(self, jsonFileName) -> None:
        super(ServerConfig, self).__init__(jsonFileName)

        self.webConfig = self.serverConfig['Web']

    def getAddress(self):
        ip = self.webConfig['BindAddress']['IP']
        port = self.webConfig['BindAddress']['Port']

        return ip, port

if __name__ == "__main__":
    cfg = ServerConfig("G:\\ServerManager\\server\\config\\config.json")
