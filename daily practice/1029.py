# age_man = int(input("input your age"))
#
# if  age_man >0 and age_man < 18:
#
#     print("小屁孩 ")
# elif age_man >= 18 and age_man <= 22:
#     print("小朋友")
# elif age_man > 22 and age_man <= 28:
#     print("小鲜肉")
# elif age_man >= 28 and age_man <= 35:
#     print("中青年")
# else:
#     print("老男人")

#格式化符号：%s,%d,%f,%x
#%s：输出字符串
#%f:输出float类型
#%d：输出int类型
#%x:输出16进制的类型

name = "neko"
print("my name is %s" % name)

score = 100
print("yr number is %d" %score)

pi = 3.1415926
#%f默认保留6位数字，会四舍五入；
print("圆周率%.2f" % pi)

num = 19
print("%x" %num)