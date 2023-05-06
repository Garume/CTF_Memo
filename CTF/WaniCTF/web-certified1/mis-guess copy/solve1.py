import collections
import socket


class Netcat:
    """ Python 'netcat like' module """

    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """
        return self.socket.recv(length).decode('utf-8')

    def write(self, data):
        self.socket.sendall(((str(data)+'\n')).encode('utf-8'))

    def close(self):
        self.socket.close()


def solve():
    nc = Netcat('guess-mis.wanictf.org', 50018)

    print(nc.read())

    d = collections.Counter()

    nc.write('1')

    nc.read()

    nc.write('0')

    begin = nc.read()
    begin = begin.split('\n')[0]
    begin = begin[begin.find('[')+1:begin.find(']')-1].split(", ")

    for j in range(1):
      nc.write('1')

      a = nc.read()
      print(f'{a=}')

      guess = []
      for i in range(j*1000, (j+1)*1000):
          guess += [i]*i

      nc.write(' '.join(map(str, guess)))

      b = ''
      while ']' not in b:
          b += nc.read()

      # print(f'{b=}')

      bb = b.split('\n')[0]
      # print(f'{bb=}')
      bbb = bb[bb.find('[')+1:bb.find(']')-1].split(", ")
      # print(bbb)
      d |= collections.Counter(list(map(int, bbb)))
      #print(f'{d=}')

    print(f'{d.most_common()=}')

    ans = begin[0] + " "
    for key,value in d.most_common()[::-1]:
        ans += str(key) + " "

    print(ans)

    nc.write('2')

    nc.write(ans)

    print(nc.read())
    print(nc.read())
    print(nc.read())


if __name__ == '__main__':
    solve()