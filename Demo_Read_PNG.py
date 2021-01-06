# Author:丁泽盛
# data:2020/10/3 11:08
with open('logo.png','rb') as src:
    with open('copy2logo.png','wb') as target:
        target.write(src.read())