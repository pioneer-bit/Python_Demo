# Author:丁泽盛
# data:2020/10/1 16:43

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))