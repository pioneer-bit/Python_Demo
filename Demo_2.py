# Author:丁泽盛
# data:2020/9/20 19:32
#转义字符
print('hello\nworld')# \+转义功能首字母 n-->newline
print('hello\tworld')#制表位为四位 /t重开一个制表位（水平制表位）
print('hello\rworld')#回车 覆盖前面的内容
print('hello\bworld')#\b 退一个格

print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello \n world')