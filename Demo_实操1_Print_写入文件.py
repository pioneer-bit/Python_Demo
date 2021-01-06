# Author:丁泽盛
# data:2020/10/5 10:36
'''1、使用print方式进行输出（输出目的地是文件）'''
fp=open('C:/迅雷下载/text.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

'''1、使用文件读写操作'''
with open('C:/迅雷下载/text1.txt','w') as file:
    file.write('奋斗成就不一样的你')