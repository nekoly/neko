# 练习1:
# 现有如下代码， 会输出什么：
# class People(object):
#       __name = "luffy"
#       __age = 18
#
# p1 = People()
# print(p1.__name, p1.__age)

# 回答：抛出没有属性异常，因为是私有变量，权限访问不了


# 练习2:
# 编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
class Student():
    __count = 0
    
    def __init__(self):
        Student.__count = Student.__count + 1
     
    def get_count(self):
        return Student.__count   


a = Student()
b = Student()
print("实例化%s个学生" % a.get_count())


# 练习3:
# 编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
class B():

    def handle(self):
        print("Hello B")


class A(B):

    def handle(self):
        super().handle()


a = A()
a.handle()
        
# 练习4:
# 模仿王者荣耀定义两个英雄类
# 要求：
#
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡(提示:这里是函数)


class Hero(object):

    def __init__(self, nickName, attackVal, lifeVal):
        self.nickName = nickName
        self.attackVal = attackVal
        self.lifeVal = lifeVal

    def attack(self, hero):
        hero.lifeVal = hero.lifeVal - 10       
        if hero.lifeVal < 0:
            print('这里是函数')
        else:
            print('攻击去掉10滴血.当前剩余%s' % hero.lifeVal)

            
hero1 = Hero('英雄1', 100, 20) 
hero2 = Hero('英雄1', 100, 10)

hero1.attack(hero2)
hero1.attack(hero2)
               
