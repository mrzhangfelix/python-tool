from time import sleep
from threading import Thread
def test(name):
	print(name,"name:{}")
	for i in range(10):
		print(i)
		sleep(1)
def main():
	thread1=Thread(name='thread1', target=test,args=("线程1",))
	thread2=Thread(name='thread2', target=test,args=("线程2",))
	thread1.start()
	print('wancheng')
	thread2.start()
	print('wancheng2')

if __name__ == '__main__':
	main()
