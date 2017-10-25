import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s=socket.socket()
	s.bind((host,port))

	s.listen()

	c , addr = s.accept()

	print("connected with " + str(addr))
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		print("client : "+ data)
		data = data.upper()	
		print('sending : ' + data)
		c.send(data.encode('utf-8'))
	c.close()      ##connection closed
	

if __name__ == '__main__':
		main()		



