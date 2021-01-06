# Author:丁泽盛
# data:2020/10/1 11:08
#(1)、交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1&s2) #两种方法

#（2）、并集操作
print(s1.union(s2))
print(s1|s2) #两种方法

#（3）、差集操作
print(s1.difference(s2)) #s1减去共有的
print(s1-s2)

#（4）、对称差集
print(s1.symmetric_difference(s2))
print(s1^s2) #s1并s2 减去共有的