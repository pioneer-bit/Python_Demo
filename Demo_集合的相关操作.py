# Author:丁泽盛
# data:2020/10/1 10:08
s={10,20,30,405,60}
'''集合元素的判断操作'''
print(10 in s) #True
print(100 in s) #False
print(10 not in s) #False

'''集合元素的新增操作'''
s.add(80) #add一次添加一个元素
print(s)
s.update({200,400,300})#添加集合
print(s)
s.update([100,99,8])#添加列表
s.update((78,64,56))#添加元组
print(s)
'''集合元素的删除操作'''
s.remove(100)#删除不存在的元素会抛异常
print(s)
s.discard(500)#删除不存在的元素不会抛异常

s.pop()#
s.clear() #全没了