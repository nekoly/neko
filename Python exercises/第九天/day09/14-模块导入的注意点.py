from first_model import show
import sys
#这种导入方式需要保证当前模块不要自定义
def show():
	print("这是当前模块")
show()
#导入的是自定义的
import random
#模块导入的注意点
#1.自定义模块名不能和系统模块相同
#2.导入功能代码不要在当前模块自定义,否则使用不了
#3.不要相互导入

# result = random.randint(1,5)
# print(result)
#模块搜索的顺序
print(sys.path)
#下节课授课内容
#包 线程 进程 StringIO ByteIO 序列化