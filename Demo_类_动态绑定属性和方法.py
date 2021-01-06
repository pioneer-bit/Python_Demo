# Author:丁泽盛
# data:2020/10/2 10:10

class Dog:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

    def sit(self):
        print(self.name+"  蹲下")
mydog=Dog('WILLI',34);
mydog.sit();

