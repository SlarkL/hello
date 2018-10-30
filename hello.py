import socket
my_ip = '127.0.0.1'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((my_ip,8080))
s.listen(1000)
new_s,addr = s.accept()
print(new_s.recv(1024),addr)
new_s.send(b"""
	HTTP/1.1 200 OK\r\n
	\r\n
	Hello,world!
	""")
new_s.close()









