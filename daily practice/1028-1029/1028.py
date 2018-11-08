neko_list = ["渣男","前任","准现任","后任"]
print(neko_list)

# 列表增加数据
neko_list.append("IT男")
print(neko_list)

# 插入指定数据
neko_list.insert(2,"小鲜肉")
print(neko_list)

my_boyfriend = ["trader","coder","IT guy"]
# neko_list.append(my_boyfriend)
# print(neko_list)

# 将列表的元素取出来，然后拼接到原有的列表里面
neko_list.extend(my_boyfriend)
print(neko_list)



#给老板订酒店与机票不被diss之解决方案

price = int(input("booking hotel"))

if price < 100:
    print("ready to book")
elif price >=100 and price < 150:
    print("should be confirmed for the boss")
else:
    print("you got fired")

# 修改元素
neko_list = [5,"伪翻译","数据分析","才华有限","photographer","bug owner","data analyst"]
neko_list[0] = "假同传"
print(neko_list)