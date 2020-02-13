import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('192.168.5.145', 12345)
sock.sendto('hello'.encode('utf-8'), server_addr)
