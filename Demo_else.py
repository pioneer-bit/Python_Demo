# Author:丁泽盛
# data:2020/9/26 11:17
for item in range(3):
    pwd=input('请输入密码：')
    if(pwd=='8888'):
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print("对不起三次密码都不正确")


