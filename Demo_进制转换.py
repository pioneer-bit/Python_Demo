# Author:丁泽盛
# data:2020/10/5 10:52
num=int(input('请输入一个十进制的整数'))#讲str类型转换成int类型
print(num,'的二进制数为',bin(num))#1、位置可变的位置参数
print(str(num)+'的二进制数为'+bin(num))#bin转完的结果就是字符串（2、+号做连接符+左右为str类型）
print('%s的二进制数为：%s'%(num,bin(num)))#3、格式化字符串
print('{0}的二进制数为{1}'.format(num,bin(num)))#3、格式化字符串
print(f'{num}的二进制数为:{bin(num)}') #3、格式化字符串

#八进制
print(f'{num}的八进制数为:{oct(num)}')
#十六进制
print(f'{num}的十六进制数为:{hex(num)}')



