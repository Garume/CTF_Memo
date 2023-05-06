import socket

class Netcat:
    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):
        """ Read 1024 bytes off the socket """
        return self.socket.recv(length)

    def write(self, data):
        self.socket.sendall(((str(data))).encode('utf-8'))

    def close(self):
        self.socket.close()



def solve():
    nc = Netcat('dsa-cry.wanictf.org', 50010)

    lines = nc.read().decode('utf-8').split("\n")
    for line in lines:
        print(line)
    
    
    lines = nc.read().decode('utf-8').split("\n")
    for line in lines:
        print(line)
    
    
    lines = nc.read().decode('utf-8').split("\n")
    for line in lines:
        print(line)



if __name__ == '__main__':
    solve()