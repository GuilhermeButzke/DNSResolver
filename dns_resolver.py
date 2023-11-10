import socket

host = input ("Digite o IP ou Host: ")

print(host, ":", socket.gethostbyname(host))