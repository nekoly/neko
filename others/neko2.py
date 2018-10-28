# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # 练习1
    # 打印单词'interested'中的每一个字母。
    my_word = "interested"
    for i in range(0, len(my_word)):
            print(my_word[i])
    
    # 练习2
    # 对列表Names = ['Bart', 'Lisa', 'Adam']中的每个名字打印Hello,xxx
    Names = ['Bart', 'Lisa', 'Adam']
    for name in Names:
        print("Hello," + name)
    
    # 练习3
    # 计算1-100内所有偶数的和。(利用循环,预习)
    i = 0
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total = i + total
    
    print("计算1-100内所有偶数的和" + str(total))
    
    # 练习4
    # 倒序输出列表[1,2,3,4,5]中的元素
    vList1 = [1, 2, 3, 4, 5]
    vList1.reverse()
    print(vList1)
    
    # 练习5
    # 编写代码，使用 if...elif...else 语句判断输入的一个数字是正数、负数或零.
    number = -10
    if number > 0:
      print("正数")
    elif number == 0:
      print("零")
    else:    
      print("负数")
      
    # 练习6
    # 根据输入年龄，对其称谓进行归类： 大于18岁，输出 adult，小于18岁，输出teenager。
    # 编写代码，使输出结果为：
    # your age is 3
    # teenager
    age = int(input("输入年龄:"))
    if(age >= 18):
      print("your age is " + str(age) + "\nadult")
    else:
      print("your age is " + str(age) + "\nteenager")      
    
    # 练习7
    # 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    # 低于18.5：过轻 18.5-25：正常 25-28：过重 28-32：肥胖 高于32：严重肥胖
    # 请用代码实现它,并实现输出结果为：
    # your bmi is: 26.285714285714285
    # 过重
    hight = 1.75
    weight = 80.5
    bmi = weight / (hight * hight)
    
    if(bmi < 18.5):
        print("your bmi is: " + str(bmi) + "\n过轻")
    elif(bmi >= 18.5 and bmi < 25): 
        print("your bmi is: " + str(bmi) + "\n正常")
    elif(bmi >= 25 and bmi < 28): 
        print("your bmi is: " + str(bmi) + "\n过重")
    elif(bmi >= 28 and bmi < 32):     
        print("your bmi is: " + str(bmi) + "\n肥胖")
    elif(bmi >= 32):
        print("your bmi is: " + str(bmi) + "\n严重肥胖")
