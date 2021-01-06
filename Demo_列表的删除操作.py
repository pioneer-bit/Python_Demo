# Author:丁泽盛
# data:2020/9/26 14:01
lst = [10,20,30,30,40,50,60,70]
lst.remove(30)#从列表中移除一个元素，如果有重复元素只移第一个元素
print(lst)

#pop 根据索引移除元素
lst.pop(1)#移除索引为1的元素
print(lst)
lst.pop()#如果不指定参数（索引），将删除列表中的最后一个元素
print(lst)

print('------------切片操作-删除至少一个元素，将产生一个新的列表对相')
new_list=lst[1:3]
print('原列表',lst)
print('新列表',new_list)

#不产生新的列表对象，而是删除原列表中的内容
lst[1:3]=[]#用空的替代
print(lst)

#清除列表中所有元素
lst.clear()
