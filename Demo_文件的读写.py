# Author:丁泽盛
# data:2020/10/2 20:10

#文件读
# with open('test.txt') as file_object:
#     contents=file_object.read()#read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来就是一个空行，删除末尾空行使用rstrip()
#     print(contents.rstrip())

#逐行读取
# filename='PI.txt'
# with open(filename) as file_object:
#     pi_string = ''
#     for line in file_object:
#         pi_string +=line.strip()
#         print(line.rstrip())
#文件写
#open第二个实参，可指定读取模式（‘r’）、写入模式（'w'）、附加模式（‘a'）、能够读取和写入文件模式（'r+'）
# 省略第二个参数，将以默认的只读打开文件
filename='write.txt'
with open(filename,'w') as file_object:
    file_object.write('I love programing.')