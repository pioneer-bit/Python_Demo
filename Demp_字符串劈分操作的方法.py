# Author:丁泽盛
# data:2020/10/1 14:46
s='hello world python'
lst=s.split()
print(lst)

s1='hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))