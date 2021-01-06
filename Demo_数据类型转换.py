# Author:丁泽盛
# coding:UTF-8
# data:2020/9/20 20:35
name='张三'
age=20


print(type(name),type(age))#说明name与age的数据类型不同
#print('我叫'+name+'今年，'+age+'岁')#当将str类型与ing类型进行连接时，报错，使用类型转换

print('我叫'+name+'今年，'+str(age)+'岁')#将int类型通过str()函数转化成str类型
