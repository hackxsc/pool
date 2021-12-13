import socketserver
import json
from utils import *

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip().decode("UTF-8")
        self.data = json.loads(data)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        if self.data['method'] == METHOD_MINING_CONFIG:
            self.return_config_method()
        elif self.data['method'] == METHOD_SUBSCRIBE:
            self.return_subscribe_method()
        elif self.data['method'] == METHOD_SUBMIT:
            self.return_submit_method()
    
    def return_config_method():
        msg = RETURN_CONFIG_STR
        print("[server]: ", msg)
        self.request.sendall(msg.encode())

    def return_subscribe_method():
        print("[server]: receive subscribe")

    def return_submit_method():
        print("return submit from miner")

if __name__ == '__main__':
    HOST, PORT = "192.168.64.128", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
