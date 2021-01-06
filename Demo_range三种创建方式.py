# Author:丁泽盛
# data:2020/9/25 20:34
#内置函数range(): 返回值时一个迭代器对象
#Range(stop)    ------>>创建一个[0,stop]之间的整数序列，步长为1
##Range(start,stop,step)    ------>>创建一个[start,stop]之间的整数序列，步长为step
r=range(10)
print(r)#range(0,10)，默认从0开始
print(list(r))

r=range(1,10)
print(r)#range(0,10)，默认从0开始
print(list(r))


r=range(1,10,2)
print(r)#range(0,10)，默认从0开始
print(list(r))

#判断指定整数在序列中是否存在 in，not in

print(10 in r)