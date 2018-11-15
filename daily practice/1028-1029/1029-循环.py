#循环 while循环 for 循环：根据条件执行某种操作
# 死循环，一直满足条件就循环（cpu)
#最常见的bug之一
# while True:
#     print("hello")

#打印0-5
#执行5次循环

num= 0
while num < 5:
    num +=1
    print(num)
print("----------------------")

#for循环 结合range来使用（range代表一个范围）
#range(0-4)
#默认：起始数据为0，结束必写，步长默认为1
# for value in range(5):
#     print(value)
#(0,6,1)0，起始数据，结束数据（结束数据不执行循环，步长（跳跃的距离）
for value in range(0,6,3):
    print(value)
#for循环可以结合while循环可以结合else语句来使用
print("-------------------")
num = 5
while num >=1:
    print(num)
    num -=1
else:
    print("The end")

for value in range(3):
    print("ok")
else:
    print("END")



