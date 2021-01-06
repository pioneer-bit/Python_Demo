# Author:丁泽盛
# data:2020/9/20 20:23

#浮点数的底层问题
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
print(n1+n2)# 此处输出3.3000000000000003
            # 解决办法如下

from decimal import  Decimal
print(Decimal('1.1')+Decimal('2.2'))

#f1=True 就是1
#f2=False 就是0
#布尔可以转化为整数计算

