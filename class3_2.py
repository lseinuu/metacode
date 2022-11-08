# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 19:42:14 2022

@author: 이세인
"""




f = open('C:/Users/이세인/OneDrive/바탕 화면/metacode-python/test.txt','r',encoding='utf8')
line = f.readlines() #빈칸 추가되서 들어와 있음
f.close()


f = open('C:/Users/이세인/OneDrive/바탕 화면/metacode-python/정보.txt','r',encoding='utf8')
line = f.readlines()
f.close()

print(line) 
# 받아온 결과의 \n를 없애본다.
#결과  ['이름:이상훈', '지역:서울', '나이:32', '성별:남']



for i in range(len(line)):
    line[i] = line[i].replace('\n','')
print(line)









result = []
for i in line:
    temp = i.replace("\n","")
    result.append(temp)


# list의 각 원소의 : 로 구분해보자
# 결과 [['이름', '이상훈'], ['지역', '서울'], ['나이', '32'], ['성별', '남']]



print(line)

result = []
for i in line:
    temp = i.split(":")
    result.append(temp)
print(result)





result2 = []    
for i in range(len(line)):
    temp = result[i].split(":")
    result2.append(temp)












#각각의 string으로 분리해본다
# 결과 ['이름', '이상훈', '지역', '서울', '나이', '32', '성별', '남']



flat_list = [obj for sub in result2 for obj in sub]









flat_list = [item for sublist in result2 for item in sublist]
