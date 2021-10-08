import pandas as pd
import numpy as np
import xlwt
import csv

traindata = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/train.csv')
testdata = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/test.csv')
data = pd.read_csv('E:/pycharm 2020.1.5\pattern recognition/gender_submission.csv')
sex = traindata[['Sex','Survived']]
pclass = traindata[['Pclass','Survived']]
age = traindata[['Age','Survived']]
num = traindata[['Cabin','Survived']]

#性别
x1 = traindata[traindata['Sex'].isin(['male'])]
x2 = traindata[traindata['Sex'].isin(['female'])]
man = len(x1)
woman = len(x2)
all = man + woman
mans = 0;womans = 0
i = 0;S = 0
while i < all:
    if sex['Sex'][i] == 'male':
        if int(sex['Survived'][i]) == 1:
            mans = mans + 1
    else:
        if int(sex['Survived'][i]) == 1:
            womans = womans + 1
    if int(sex['Survived'][i]) == 1:
        S = S + 1
    i = i + 1
S1 = mans/man
S2 = womans/woman

#客舱等级
i = 0;pclass1 = 0;pclass2 = 0;pclass3 = 0
while i < all:
    if int(pclass['Pclass'][i]) == 1:
        pclass1 = pclass1 + 1
    elif int(pclass['Pclass'][i]) == 2:
        pclass2 = pclass2 + 1
    else:
        pclass3 = pclass3 + 1
    i = i + 1
i = 0;pclass1S = 0;pclass2S = 0;pclass3S = 0
while i < all:
    if int(pclass['Pclass'][i]) == 1:
        if int(pclass['Survived'][i]) == 1:
            pclass1S = pclass1S + 1
    elif int(pclass['Pclass'][i]) == 2:
        if int(pclass['Survived'][i]) == 1:
            pclass2S = pclass2S + 1
    elif int(pclass['Pclass'][i]) == 3:
        if int(pclass['Survived'][i]) == 1:
            pclass3S = pclass3S + 1
    i = i + 1
P1 = pclass1S/pclass1
P2 = pclass2S/pclass2
P3 = pclass3S/pclass3

#年龄
i = 0;sum = 0
all1 = all
while i < all:
    if pd.isnull(age['Age'][i]):#判断是否为空
        all1 = all1 - 1
    else:
        sum = sum + age['Age'][i]
    i = i + 1
a1 = sum/all1
if a1 < 15:
    a1 = 'young'
elif 15 <= a1 < 55:
    a1 = 'middle'
else:
    a1 = 'old'

age1 = {}
i = 0;young = 0;middle = 0;old = 0
while i < all:
    if float(age['Age'][i]) < 15:
        age1[i] = 'young'
        young = young + 1
    elif 15 <= float(age['Age'][i]) < 55:
        age1[i] = 'middle'
        middle = middle + 1
    elif float(age['Age'][i]) >= 55:
        age1[i] = 'old'
        old = old + 1
    elif pd.isnull(age['Age'][i]):
        age1[i] = a1
        if a1 == 'young':
            young = young + 1
        elif a1 == 'middle':
            middle = middle + 1
        else:
            old = old + 1
    i = i + 1
i = 0;youngs = 0;middles = 0;olds = 0
while i < all:
    if age1[i] == 'young':
        if int(age['Survived'][i]) == 1:
            youngs = youngs + 1
    elif age1[i] == 'middle':
        if int(age['Survived'][i]) == 1:
            middles = middles + 1
    else:
        if int(age['Survived'][i]) == 1:
            olds = olds + 1
    i = i + 1
A1 = youngs/young
A2 = middles/middle
A3 = olds/old

#客舱号
i = 0;S11 = 0;S22 = 0
number = {}
while i < all:#判断有无客舱号
    if pd.isnull(num['Cabin'][i]):
        number[i] = 0
        S22 = S22 + 1
    else:
        number[i] = 1
        S11 = S11 + 1
    i = i + 1
i = 0;S1S = 0;S2S = 0
while i < all:
    if number[i] == 1:
        if num['Survived'][i] == 1:
            S1S = S1S + 1
    else:
        if num['Survived'][i] == 1:
            S2S = S2S + 1
    i = i + 1
N1 = S1S/S11
N2 = S2S/S22

print(A1,A2,A3,S1,S2,N1,N2,P1,P2,P3)
survive = {}
survive1 = testdata[['PassengerId','Sex']]
survive1 = survive1.to_dict(orient = 'records')


i = 0
while i < all:
    if sex['Sex'][i] == 'male':
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S1*P1*A1*N1
                    p2 = (1 - S1) * (1 - P1) * (1 - A1) * (1 - N1)
                else:
                    p1 = S1*P1*A1*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P1*A2*N1
                    p2 = (1 - S1) * (1 - P1) * (1 - A2) * (1 - N1)
                else:
                    p1= S1*P1*A2*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P1*A3*N1
                    p2 = (1 - S1) * (1 - P1) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P1*A3*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A3) * (1 - N2)
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S1*P2*A1*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A1) * (1 - N1)
                else:
                    p1 = S1*P2*A1*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P2*A2*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A2) * (1 - N1)
                else:
                    p1 = S1*P2*A2*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P2*A3*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P2*A3*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A3) * (1 - N2)
        else:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S1*P3*A1*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A1) * (1 - N1)
                else:
                    p1 = S1*P3*A1*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P3*A2*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A2) * (1 - N1)
                else:
                    p1 = S1*P3*A2*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P3*A3*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P3*A3*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A3) * (1 - N2)
    else:
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P1 * A1 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P1 * A1 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P1 * A2 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P1 * A2 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P1 * A3 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P1 * A3 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A3) * (1 - N2)
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P2 * A1 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P2 * A1 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P2 * A2 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P2 * A2 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P2 * A3 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P2 * A3 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A3) * (1 - N2)
        else:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P3 * A1 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P3 * A1 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P3 * A2 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P3 * A2 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P3 * A3 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P3 * A3 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A3) * (1 - N2)
    if p1 > p2:
        survive[i] = 1
    else:
        survive[i] = 0
    i = i + 1
#计算准确率
TP = 0;TN = 0;FP = 0;FN = 0
i = 0
while i < all:
    if survive[i] == int(traindata['Survived'][i]):
        if survive[i] == 1:
            TP = TP + 1
        else:
            TN = TN + 1
    else:
        if survive[i] == 1:
            FP = FP + 1
        else:
            FN = FN + 1
    i = i + 1
Accuracy_train = (TP + TN)/(TP + TN + FP + FN)
print('Accuracy =',Accuracy_train)



#测试集
i = 0
res = testdata.shape[0]
print(res)
while i < all:
    if sex['Sex'][i] == 'male':
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                if number[i] == 1:
                    survive1
                else:
                    p1 = S1*P1*A1*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P1*A2*N1
                    p2 = (1 - S1) * (1 - P1) * (1 - A2) * (1 - N1)
                else:
                    p1= S1*P1*A2*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P1*A3*N1
                    p2 = (1 - S1) * (1 - P1) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P1*A3*N2
                    p2 = (1 - S1) * (1 - P1) * (1 - A3) * (1 - N2)
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S1*P2*A1*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A1) * (1 - N1)
                else:
                    p1 = S1*P2*A1*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P2*A2*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A2) * (1 - N1)
                else:
                    p1 = S1*P2*A2*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P2*A3*N1
                    p2 = (1 - S1) * (1 - P2) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P2*A3*N2
                    p2 = (1 - S1) * (1 - P2) * (1 - A3) * (1 - N2)
        else:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S1*P3*A1*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A1) * (1 - N1)
                else:
                    p1 = S1*P3*A1*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S1*P3*A2*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A2) * (1 - N1)
                else:
                    p1 = S1*P3*A2*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S1*P3*A3*N1
                    p2 = (1 - S1) * (1 - P3) * (1 - A3) * (1 - N1)
                else:
                    p1 = S1*P3*A3*N2
                    p2 = (1 - S1) * (1 - P3) * (1 - A3) * (1 - N2)
    else:
        if int(pclass['Pclass'][i]) == 1:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P1 * A1 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P1 * A1 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P1 * A2 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P1 * A2 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P1 * A3 * N1
                    p2 = (1 - S2) * (1 - P1) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P1 * A3 * N2
                    p2 = (1 - S2) * (1 - P1) * (1 - A3) * (1 - N2)
        elif int(pclass['Pclass'][i]) == 2:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P2 * A1 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P2 * A1 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P2 * A2 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P2 * A2 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P2 * A3 * N1
                    p2 = (1 - S2) * (1 - P2) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P2 * A3 * N2
                    p2 = (1 - S2) * (1 - P2) * (1 - A3) * (1 - N2)
        else:
            if age1[i] == 'young':
                if number[i] == 1:
                    p1 = S2 * P3 * A1 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A1) * (1 - N1)
                else:
                    p1 = S2 * P3 * A1 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A1) * (1 - N2)
            elif age1[i] == 'middle':
                if number[i] == 1:
                    p1 = S2 * P3 * A2 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A2) * (1 - N1)
                else:
                    p1 = S2 * P3 * A2 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A2) * (1 - N2)
            else:
                if number[i] == 1:
                    p1 = S2 * P3 * A3 * N1
                    p2 = (1 - S2) * (1 - P3) * (1 - A3) * (1 - N1)
                else:
                    p1 = S2 * P3 * A3 * N2
                    p2 = (1 - S2) * (1 - P3) * (1 - A3) * (1 - N2)
    if p1 > p2:
        survive[i] = 1
    else:
        survive[i] = 0
    i = i + 1
#导出
header = ['PassengerId', 'Survived']
with open('E:/pycharm 2020.1.5\pattern recognition/submission2.csv', 'a', newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=header) # 提前预览列名，当下面代码写入数据时，会将其一一对应。
    writer.writeheader()  # 写入列名
    writer.writerows(survive1)
'''
#导出
pf = pd.DataFrame(list(survive1))#将字典列表转换为DataFrame
order = ['PassengerId','Survived']
pf = pf[order]
file_path = pd.ExcelWriter('E:/pycharm 2020.1.5\pattern recognition/submission.xlsx')#指定生成的Excel表格名称
pf.fillna(' ',inplace = True)#替换空单元格
pf.to_excel(file_path, encoding='utf-8', index=False)# 输出
file_path.save()#保存表格
'''