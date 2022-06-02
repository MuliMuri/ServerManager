from tornado import web, ioloop, httpserver


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("app")

    def post(self):
        pass


# TODO: more thread/process to run the web_server (one by one) in the furture
# BUG: The MainProcess can't do the SubProcess's functions. Need to set sth label, SubProcess use if to check it
class ServerWeb():
    def __init__(self, ip, port) -> None:
        def _app_server():
            _app = web.Application([
                (r"/", IndexHandler)
            ])

            _server = httpserver.HTTPServer(_app)
            _server.listen(port, ip)

            return _server

        self.web = _app_server()

    def start(self):
        ioloop.IOLoop.current().start()

    def stop(self):
        ioloop.IOLoop.current().stop()

    def reboot(self):
        ioloop.IOLoop.current().stop()
        ioloop.IOLoop.current().start()



def make():
    server_web = ServerWeb("127.0.0.1", 8080)
    server_web.start()
    
if __name__ == "__main__":
    
    from multiprocessing import Process

    server_web_process = Process(target=make)

    server_web_process.start()

    print("BreakPoint")
