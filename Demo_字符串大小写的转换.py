# Author:丁泽盛
# data:2020/10/1 14:31
s='hello python'
a=s.upper() #转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))

b=s.lower()#转成小写之后，会产生一个新的字符串对象
print(s,id(b))
print(s,id(s))

s2='hello,Python'
print(s2.swapcase())#小写变大写 大写变小写
print(s2.title())#把每个单词以一个字符传换成大写，把每个单词剩余字符传换成小写