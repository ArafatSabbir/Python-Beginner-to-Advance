import socket

myk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myk.connect(('data.pr4e.org',80))
cm = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
myk.send(cm)

while True:
    data = myk.recv(512)
    if(len(data)<1):
        break
    print(data.decode())

myk.close()