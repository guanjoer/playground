import socket

HOST = '127.0.0.1'

PORT = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n')

res = client.recv(4096)

print(res.decode('utf-8'))
client.close()