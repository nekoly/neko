#定义一个空的字典
ly_dict = {}
print(ly_dict,type(ly_dict))

#给字典增加键值对
ly_dict["name"] = "neko"
#key是唯一的(如果增加重复，会更新value)
# ly_dict["name"] = "ly"
ly_dict["age"] = 18
ly_dict["sex"] = "male"
ly_dict["address"] = "HK"
print(ly_dict)

#修改键字对
ly_dict["age"] = 28
print(ly_dict)

#删除(删除整个字典）
# a = 10
# del a
# print(a)
# del ly_dict
# print(ly_dict)
del ly_dict["age"]
print(ly_dict)

ly_dict = {"name":"neko","age":18,"sex":"female"}
#随机删除
# result = ly_dict.popitem()
# print(ly_dict,result)

#指定数据删除
value = ly_dict.pop("age")
print(ly_dict,value)

#获取所有的value
result = ly_dict.values()
print(result)

#获取所有的key
yao = ly_dict.keys()
print(yao)

#判断key是否在字典里

result = "ouki" in ly_dict
print(result)
























