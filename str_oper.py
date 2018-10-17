# my_neko="jkfledcjuuijfkldsjfuopslfjlwrtertgbvfjds"
# result=my_neko.index("e")
# print(result)
#
#
# result=my_neko.find("z")
# print(result)

# find如果没有找到数据那么返回的结果为-1，index如果没找到返回的结果，那么程序崩溃

#统计字符串的长度，个数

my_neko="jkfledcjuuijfkldsjfuopslfjlwrtertgbvfjds"
result=len(my_neko)
print(result)

#统计某个字符串出现的次数

result=my_neko.count("f")
print(result)

#替换指定数据

result=my_neko.replace("f","888")
print(result)

#分割数据
my_neko="apple,pear,orange"
result=my_neko.split(",")
print(result)

