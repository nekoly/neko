# -*- coding: utf-8- -*-

#NO.1

# def neko():
#     return"hello,neko"
# a=neko()
# print(a)

#NO.2

# def neko01(a,b,c):
#     return(a-b-c)
# a=neko01(3,4,9.3)
# # a=int(neko01(3,8,9.3)) 计算结果取整
# print(a)


#NO.3
""" 首先neko，neko01是函数，而且他们都有参数传入，
第二，neko01参数有默认值1.25，如果外部有传值，以外部的值传入，
不传才用1.25，neko01(wight=8)，这个会用变量值8覆盖1.25的值。
这两个函数，neko函数，是直接将调用的值赋值给wight，neko01是指定哪个参数值赋值传入。
"""

def neko(wight):
    a=wight*9.8
    print(a)
neko(5.3)

def neko(wight=46):
    a=wight-3
    print(a)
neko(50)




# def su(wight):
#     bodywight=wight*2
#     print(bodywight)
# su(75)


# def converter(wight):
#     ponds=wight/0.45
#     print(ponds)
# converter(100)
#
#
# def neko(wight):
#     a=wight/0.25+1
#     print(a)
# neko(66.39)
# neko(34)
# neko(555)
# neko(888)
#
# def neko01(wight=1.25):
#     a=wight/4+1
#     print(a)
# neko01(wight=8)






