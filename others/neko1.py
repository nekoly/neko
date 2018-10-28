# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # 练习1
    # 创建两个列表，列表1含有字符串'life','is','short'，列表2含有字符串'you','need','python'。并输出'need'
    vlist1 = ["life", "is", "short"]
    vlist2 = ["you", "need", "python"]
    print(vlist2[1])
    
    # 练习2
    # 截取列表['a','b','c','d']中的前三个元素。
    vlist3 = ['a','b','c','d']
    print(vlist3[:3])
    
    # 练习3
    # 对已给字典dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}，
    # 增加 Age=8 与 School= DPS School 两键值对，并输出。
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    dict['Age']=8
    dict['School']='DPS School'
    print(dict)
     
    # 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下:
    # 输出结果样例为：
    # dict['Age']:  8
    # dict['School']:  DPS School
    dict.pop("Age")
    dict.pop("School")
    print(dict)
    
    # 练习4
    # 用while...else...语句编写一个程序，判断输入数字是奇数还是偶数。
    i=1
    while i <= 100:
     if (i % 2) == 0:
         print("数字"+str(i)+"是偶数")
     else:
         print("数字"+str(i)+"是奇数")
     i=i+1
    
    
