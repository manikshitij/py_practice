import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('216.250.120.69', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()