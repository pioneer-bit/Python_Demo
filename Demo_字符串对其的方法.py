# Author:丁泽盛
# data:2020/10/1 14:40

s='hellp python'
'''居中对齐'''
print(s.center(20,"*"))
'''左对齐'''
print(s.ljust(20,'*'))
print(s.ljust(10))#不设定默认填充就是空格
'''右对齐'''
print(s.rjust(20,'*'))
'''zfill 也是右对齐使用0进行填充'''
print(s.zfill(40))