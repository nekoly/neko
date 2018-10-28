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

#判断是否以指定数据开头

my_url="https://github.com/"
result=my_url.startswith("http")
print(result)

result=my_url.endswith(".com/")
print(result)


#把字符串以指定字符串分割成为三部分

my_neko = "aaabcccddd"
result=my_neko.partition("d")
print(result)

#把根据指定字符串拼接数据，前提是最终的数据是字符串

#指定字符串数据

ouki_ly="-"
my_neko="wuteokvmkbnouwerp"
result=ouki_ly.join(my_neko)
print(result)

my_neko=("5","e","j")
result=ouki_ly.join(my_neko)
print(result)


