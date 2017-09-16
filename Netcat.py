#Netcat class is not my code, here's the link to it: https://gist.github.com/leonjza/f35a7252babdf77c8421

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
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()



# start a new Netcat() instance
'''
nc = Netcat('misc.chal.csaw.io', 4239)
import time

ii = 0
ss = ''
while (True):
    s = nc.read(11)
    ii += 1
    s0 = s[0:9]
    print(s0)
    i = 0
    for e in range(len(s0)):
        if s0[e] == '1':
            i += 1
    if i == 0 and ii > 15:
        print(ss)
        break
    elif i%2 == 0:
        ss += '1'
        nc.write('1')
    else:
        ss += '0'
        nc.write('0')
    nc.read(1)
'''

