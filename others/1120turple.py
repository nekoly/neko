#list []

mylist = [1,2,3,4,5]

#turple ()

myturple = (1,2,3,4,5)

print(type(mylist))
print(type(myturple))

print(len(mylist))
print(len(myturple))

print(mylist[1])
print(myturple[1])

# print(dir(mylist))
#
# print("&&&&&&&&&&&&&&&&&&&&&&&&&")
#
# print(dir(myturple))

#list is mutable：list可以更改数据类型
#tuple is innutable:tuple不可以更改数据类型

mylist.remove(2)
print(mylist)

myturple.remove(2)
print(myturple)
