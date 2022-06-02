from config.config import ServerConfig
from web.web import ServerWeb


class ServerSystem():
    def __init__(self) -> None:
        self.serverConfig = ServerConfig("G:\\ServerManager\\server\\config\\config.json")
        self.web = None
        
        self.__make_web()

    def __make_web(self):
        ip, port = self.serverConfig.getAddress()
        self.web = ServerWeb(ip, port)
        self.web.start()


if __name__ == "__main__":
    srv = ServerSystem()
