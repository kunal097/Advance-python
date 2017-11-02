from socket import socket , AF_INET,SOCK_DGRAM


def main():
	host='127.0.0.1'
	port = 5001

	server=('127.0.0.1',5000)


	s = socket(AF_INET,SOCK_DGRAM)

	s.bind((host,port))

	msg = input("Client : ")

	while msg != 'q':
		s.sendto(msg.encode('utf-8'),server)

		data , addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print('Server : ' + data )
		msg = input("client : ")
	s.close()
	

if __name__ == '__main__':
	main()		