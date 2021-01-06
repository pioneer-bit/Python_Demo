# Author:丁泽盛
# data:2020/9/26 14:44
lst=[20,40,23,12,42,56]
print('排序前的列表',lst,id(lst))

#开始排序
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print(lst)