# Author:丁泽盛
# data:2020/9/20 19:19

#输出数字
print(520)

#输出字符串
print('hello world') #不需要理解，直接输出
#不进行换行输出
print('hello','你好','这样')

#含有运算符的表达式
print(3+1) #输出表达式的结果

#将数据输出到文件中
# #注意点 使用file=fp
#不进行换行输出
fp=open('C:/迅雷下载/text.txt','a+') #a+ 如果文件不存在就创建，存在就在文件的内容后面追加
print('hello world',file=fp)
fp.close()