from socket import socket , AF_INET,SOCK_DGRAM


def main():
	host = '127.0.0.1'
	port = 5000

	s=socket(AF_INET,SOCK_DGRAM)
	s.bind((host,port))

	print("Server started : ")
	while True:
		data,addr = s.recvfrom(1024)
		data=data.decode('utf-8')
		print("msg from : "+ str(addr))
		print('from connected user : '+ data)
		data = data.upper()
		print('sending : ' + data)
		s.sendto(data.encode('utf-8'),addr)
	s.close()

if __name__ == '__main__':
	main()

