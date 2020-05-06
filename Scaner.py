import socket
import sys
mac = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993]
print('Start')
host = input('Pls  enter text IP or name Domain: ')
print ('------------------------------')
print ('Scaning ports')
print ('------------------------------')
for port in mac:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        pass
    else:
        s.close
        print(host + ':' + str(port) + ' port active')
print ('------------------------------')
print ('END')