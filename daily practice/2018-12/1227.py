# -*- coding: utf-8- -*-

#第三种
def converter(wight):
    ponds=wight/0.45
    print(ponds)
converter(100)


def neko(wight):
    a=wight/0.25+1
    print(a)
neko(66.39)
neko(34)
neko(555)
neko(888)

def neko01(wight=1.25):
    a=wight/4+1
    print(a)
neko01(wight=8)


#第一种
def neko():
    return"hello,neko"
a=neko()
print(a)

#第二种
def su(a,b,c):
    return(a+b+c)
a=su(1,2,3,)
print(a)

