# -*- coding: utf-8- -*-

#第三种
"""
首先neko，neko01是函数，而且他们都有参数传入，
第二，neko01参数有默认值1.25，如果外部有传值，
以外部的值传入，不传才用1.25，neko01(wight=8)，这个会用变量值8覆盖1.25的值。
这两个函数，neko函数，是直接将调用的值赋值给wight，neko01是指定哪个参数值赋值传入

"""
#no.1
def neko(wight):
      a=wight/0.25+1
      print(a)
neko(66.39)
neko(56)
neko(123)

#no.2
def neko01(wight=1.25):
      a=wight*0.5
      print(a)
neko(8)


def converter(wight):
    ponds=wight/0.45
    print(ponds)
converter(100)


def neko(wight):
    a=wight/0.25+1
    print(a)
neko(66.39)
neko(34)
neko(555)
neko(888)

def neko01(wight=1.25):
    a=wight/4+1
    print(a)
neko01(wight=8)


#第一种
def neko():
    return"hello,neko"
a=neko()
print(a)

#第二种
def su(a,b,c):
    return(a+b+c)
a=su(1,2,3,)
print(a)

