# Author:丁泽盛
# data:2020/10/13 20:48
import csv
import random

with open('Prostate_Cancer.csv', 'r') as file:
    reader = csv.DictReader(file)  # 以字典的方式读这个文件
    datas = [row for row in reader]  # //把信息取出来放到datas里面，相当于一个list

    print(datas)

random.shuffle(datas)  # 每次运行都将这个数据集打乱一下

n = len(datas) // 3  # '/'结果有小数点; '//'是整除结果无小数点

test_set = datas[0:n]  # 前三分之一为测试集
train_set = datas[n:]  # 后三分之二为训练集


# 传入d1和d2两个单个字典，算出两者的距离
def distance(d1, d2):  # 算的是欧式距离
    res = 0
    for key in ("radius", "texture", "perimeter", "area", "smoothness", "compactness", "symmetry",
                "fractal_dimension"):
        res += (float(d1[key]) - float(d2[key])) ** 2  # '**'平方
        return res ** 0.5


k = 7


# 传入单个字典，算出这个字典（未知）和训练集（已知）之间的关系
# 求出后，排序，选出前k个，加权平均
def knn(data):
    res = [  # res里面是训练集的结果标签和data与训练集的距离
        {"result": train["diagnosis_result"], "distance": distance(data, train)}
        for train in train_set
    ]
    # 升序排序
    sorted(res, key=lambda item: item['distance'])
    # 取前k个值
    res2 = res[0:k]
    # 加权平均（result是最终判断依据）
    result = {'B': 0, 'M': 0}
    # 总距离
    sum_dist = 0
    for r1 in res2:
        sum_dist += r1['distance']
    # 逐个分类加权
    for r2 in res2:
        result[r2["result"]] += 1 - r2["distance"] / sum_dist
    # print(result)
    if result['B'] > result['M']:
        return 'B'
    else:
        return 'M'


# 测试
for r3 in test_set:
    d = knn(r3)
    print(d, r3["diagnosis_result"])

correct = 0
for test in test_set:
    result1 = test['diagnosis_result']
    result2 = knn(test)

    if result1 == result2:
        correct = correct + 1
print(str(correct / len(test_set)))
