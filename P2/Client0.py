import socket
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port =port
    def ping(self):
        print('OK!')
    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print('server is up')
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)
    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To Server:", msg)
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        return "From server: " + response

    def debug_talk(self, msg):
        response = self.talk(msg)
        color_response = colored(response, 'green')
        print('From Server: ', color_response)