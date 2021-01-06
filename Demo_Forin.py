# Author:丁泽盛
# data:2020/9/26 10:55
for item in 'PYTHON':
    print(item)

#range() 产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不许呀使用到自定义变量，可将自定义变量写为'_'
for _ in range(5):
    print('hello world')
