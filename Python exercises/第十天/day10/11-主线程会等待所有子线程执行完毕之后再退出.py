import threading
import time

def AA():
	#打印在哪个线程执行的方法
	print("AA",threading.current_thread())
	print("这是在子线程执行的")
	while True:
		print("AA")
		time.sleep(0.2)


if __name__ == '__main__':

	print("main",threading.current_thread())

	#创建子线程执行AA函数
	t1 = threading.Thread(target=AA)
	#设置守护线程,主线程退出会直接销毁子线程不执行相对应的代码
	#线程开启之前进行相对应的操作
	t1.setDaemon(True)
	t1.start()


	#执行了over代表主线程结束
	time.sleep(1)
	print("over")