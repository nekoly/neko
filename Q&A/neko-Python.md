
1.
 del ly_list[1]
print(ly_list)

为什么这个前面不用result?
明确地说，del是操作命令不是函数 至于是使用函数调用方式还是用命令的方式这并不重要， 比如python2 里面 print 是命令，python3里print（）就成函数了，但是背后实现的机制并没有什么不同。
https://bbs.csdn.net/topics/392304121

2.
neko_tuple = (5,23,"ly",True,4.6)
print(neko_tuple,type(neko_tuple))

#根据下标取值

value = neko_tuple[1]
print(value)

为什么这里又变成value？
Value和result, del ly_list三种用法怎么区别？什么时候用value，result或者什么都不用？
1. value = neko_tuple[1]，有等号是赋值的意思，把neko_tuple[1]的值赋值到value变量，print(value)就控制台输出value的内容，
变量的意思是把数据存放到这个标识里，后面可以用这个标识找到数据。不用每次取值都用这个neko_tuple[1]，可以理解为是简化代码一个方法。代码设计有个原则是写的越少越好，功能能实现。

这个value和result也可以改成ly对么？
可以的，只是一个标识，只要以字母开头的变量。



3.在
#打印0-5
#执行5次循环

num= 0
while num < 5:
    print(num)
    num += 1

0
1
2
3
4

num= 0
while num < 5:
    num +=1
    print(num)
    

1
2
3
4
5

为什么在print(num)后面的num+=1还会被执行呢？
4.










