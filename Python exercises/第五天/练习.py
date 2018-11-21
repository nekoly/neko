# -*- coding: utf-8 -*-
# 练习1
# 定义一个函数，输入不定个数的数字，返回所有数字的和。
def inputNumber():
    total = 0
    vNumber = input("输入不定的数字(空格分割):")
    for i in vNumber.split(' '):
        if i:
            total = total + float(i)
    print('数字总和为:' + str(total))


inputNumber()
        
# 练习2
# 简述你对global理解
# global修改作用域为全局变量，在局部要对全局变量修改，需要在局部也要先声明该全局变量，使用关键词。


# 练习3
# 编写一个函数，输入n为偶数时，返回函数,用返回的函数求1/2+1/4+...+1/n,当输入n为奇数时，返回函数,调用返回的函数1/1+1/3+...+1/n
def fun3(n):
    total = 0
    if(n % 2 == 0):
     # 偶数
     # 1/2+1/4+...+1/n
     for i in range(2, n + 1, 2):
        total = 1 / i + total
    else:    
     # 奇数
     # 1/1+1/3+...+1/n
     for i in range(1, n + 1, 2):
        total = 1 / i + total
        
    return total


vNumber = int(input("输入一个n整数:"))
fun3(vNumber)


# 练习4
# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def fun4(obj):
    if len(obj) >= 5 :
        print('长度大于5')
        return True
    else:
        print('长度小于5')
        return False


fun4((1, 2, 3))
    
# 练习5
# 使用匿名函数对1~1000求和，代码力求简洁。
from functools import reduce
print(reduce(lambda x, y: x + y, range(1, 1001)))


# 练习6
# 指明下方函数的调用顺序
def func(name):

     def inner_func(age):
         print('name:' + name + ',age:' + str(age))

     return inner_func


new_func = func('the5fire')
new_func(26)
