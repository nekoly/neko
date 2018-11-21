import threading
#子线程和主线程会产生资源竞争
#创建互斥锁:保证同一时刻,只有一个线程去执行代码
#这样全局变量不会存在资源竞争的问题
lock = threading.Lock()
g_num = 0

def AA():
	#上锁

	global g_num
	for i in range(1000000):
		lock.acquire()

		g_num+=1
		lock.release()
	# 释放锁

	print("AA",g_num)

#200000
def BB():

	global g_num
	for i in range(1000000):
		#上锁放到for循环
		lock.acquire()
		g_num += 1
		lock.release()


	print("BB", g_num)

#进程 复习 讲作业题 html css js

if __name__ == '__main__':
    #创建两个线程
	first_thred =threading.Thread(target=AA)
	second_thred=threading.Thread(target=BB)
	first_thred.start()
	second_thred.start()



