import socket, json, random, datetime, hashlib, sys

class Server:

    def main(self):
        #take in args
        ip = sys.argv[1]
        port = int(sys.argv[2])
        accFile = sys.argv[3]
        sesTimeout = int(sys.argv[4])
        rootDir = sys.argv[5]
        self.start()

    def start(ip,port):
        #start the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip,port))
        s.listen(10)
        
        while True:
            c, addr = s.accept()

    def post():

    def get():


