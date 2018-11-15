#continue：结束本次循环，然后继续下一个循环，整个循环不一定结束

num = 0
while num <5:
    num += 1
    if num==2:
        continue
    print(num)
else:
    print("end the circulation")

#break: 跳出整个循环(结束）
num = 0
while num <= 5:
    num+=1
    if num ==2:
        break
    print(num)
