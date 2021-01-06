# Author:丁泽盛
# data:2020/10/1 9:27

'''可变序列：列表，字典'''
lst=[10,20,55]
print(id(lst))
lst.append(300)
print(id(lst))  #内存地址不发生改变



'''不可变序列  字符串，元组'''
s='hello'
print(id(s))
s=s+' world'
print(id(s))
print(s) #内存地址发生了改变