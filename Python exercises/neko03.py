# -*- coding: utf-8 -*-
# 练习2
def fun2(tupleArgs):
    total = 0
    for tupleArg in tupleArgs:
        total = total + float(tupleArg)
    return total


# 练习3:
def fun3(flag="求和", *inputmembers, **inputmemberDict):
    total = sum(inputmembers)
    
    total2 = 0
    for member in inputmemberDict:
        total2 = total2 + inputmemberDict[member]
    
    return {'total':total, 'total2':total2}


# 练习4:
def fun4(n):
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

        
if __name__ == '__main__':
    # 练习1
    # 判断下列选项调用函数正确与否，并给予说明。
    # A: abs() B:abs(-1.4) C:abs(-1,-3) D:abs('a')
    # 注:abs()绝对值函数,可以百度查询相关规则
    # abs(参数：数值类型参数)
    print('练习1:' + str(abs(-1.4)))
    
    # 练习2
    # 定义一个函数，输入不定个数的数字，返回所有数字的和。
    tupleArg = input("输入不定个数的数字(空格间隔):")
    tupleArgs = tupleArg.split(' ')
    total = fun2(tupleArgs)
    print('总和为' + str(total))
    
    # 练习3(传入不定长参数返回计算结果,使用不定长位置参数和关键字参数两种方式)
    # 定义一个函数，内置求和函数sum()。
    _dict = fun3('求和', 1, 2, 3.1, 4.1, member1=1, member2=2.1, member3=3.1)
    print('练习3:不定长位置参数求和:' + str(_dict['total']) + ',不定长关键字求和:' + str(_dict['total2']))
    
    # 练习4
    # 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...
    total = fun4(10)
    print('练习4结果:' + str(total))
