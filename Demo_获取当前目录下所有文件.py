# Author:丁泽盛
# data:2020/10/3 11:38
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename in lst:
        print(filename)