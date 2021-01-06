# Author:丁泽盛
# data:2020/10/1 15:21
#(1)%占位符
name='张三'
age=20
print('我叫%s,今年%d岁'%(name,age))

#(2){}
print('我叫{0},今年{1}岁'.format(name,age))

#(3)f-string
print(f"我叫{name},今年{age}岁")