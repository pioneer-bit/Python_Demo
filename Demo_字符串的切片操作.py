# Author:丁泽盛
# data:2020/10/1 15:12

s='hello,Python'
s1=s[:5] #由于没有指定起始位置，所以从零开始切
s2=s[6:]#由于没有指定结束位置，所以切到字符串的最后一个元素
s3='!'
newstr=s1+s2+s3
print(newstr)
'''切片[start:end:step]'''
print(s[1:5:1])