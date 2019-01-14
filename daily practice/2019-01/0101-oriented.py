# -*- coding: utf-8 -*-

class Neko():
    def study(self):
        print("neko learning Python")

    def love(self):
        print("neko love Python")

    def su(self):
        print("su is a professional coder")

    def name(self):
        print("my name is neko")

    def ablity(self):
        print("interpreter and coding")


# Neko().study()
# Neko().ablity()
#
# ly=Neko()
# ly.study()
#
# ly=Neko()
# ly.ablity()

class neko01():
    def food(self, name):
        print(name + "haha")


neko01().food("vegetable")


class neko02():
    def book(self, name):
        print(name + "ly")


neko02().book("liuyao")


class neko03():
    def city(self, name):
        print(name + ":town")


neko03().city("wuzhou")


class neko04():
    def love(self, reason,age):
        print(reason + "best"+" my age is ")


neko04().love("you are the " ,"18")


# city="hk"
# print(city.upper())


def neko(a, b, c):
    return (a + b + c)


a = neko(5, 6, 7)
print(a)
