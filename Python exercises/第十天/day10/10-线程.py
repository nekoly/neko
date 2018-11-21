#线程:执行代码的分支,默认只有一个线程,(主线程)
#python本质没有多线程(假象)
import threading
import time

def AA(count):
	for i in range(count):
		print("aa")
		time.sleep(0.2)

def BB(count):

	for i in range(count):
		print("bb")
		time.sleep(0.2)


if __name__ == '__main__':

	#创建一个子线程执行相对应的代码
	sub_thred = threading.Thread(target=AA,args=(10,))
	#启动线程(执行子线程的操作)
	#创建一个子线程
	three_thread = threading.Thread(target=BB,kwargs={"count":5})
	sub_thred.start()
	three_thread.start()

	#在主线程调用函数






#线程是无须的,由cpu调度