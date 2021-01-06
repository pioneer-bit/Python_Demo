# Author:丁泽盛
# data:2020/10/2 16:11
import time
import urllib.request
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())

