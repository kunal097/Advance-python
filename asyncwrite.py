import threading
import timer


class AsyncWrite(threading.Thread):
	def __init__(self,text,out):
		threading.Thread.__init__(self)
		self.text=text
		self.out=out

	def run(self):
		f = open(self.out,'a')
		f.write(self.text + '\n')
		f.close()
		timer.time.sleep(2)
		print("Finish background writing process ")
			

def main():
	msg = input("Enter message : ")
	back_thrd=AsyncWrite(msg,'out.txt')
	back_thrd.start()

	print("The program can continue after completing background job ")


	back_thrd.join()
	print("waited until thread completed")


if __name__ == '__main__':
		main()	
