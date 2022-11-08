# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:55:43 2022

@author: 이세인

"""
# 파이썬 개발환경(IDE) : Spyder(Anaconda), PyCharm, JupyerNotebook
# Matlab layout, Variable explorer로 변수 확인 가능
# F5 : 전체실행, F9 : 커서나 드래그 한 부분만 실행


# 1) 숫자형의 종류
# int() : 정수
# float() : 실수

a = int(3)
b = 4  #그냥 숫자 정수를 넣고 싶을 때는 굳이 int()안 써도 int형으로 들어간다는 것을 알 수 있다.
c = float(2)
d = 2.0 #float형도 마찬가지


# 정수와 실수의 덧셈 뺄셈의 결과는 실수
e = a + c #a의 값이 궁금해질 때는 a만 드래그한 후 F9 눌러주면 확인 가능★
f = a - c
g = a * c
h = c / d  #1.0


# 산술연산자
# a//b : a를 b로 나눈 몫
4//3  #1
# a%b : a를 b로 나눈 나머지
4%3   #1
# a**b : a의 b승
4**3  #64


# Boolean(불리안, 참/거짓)   # 컴퓨터는 불리안으로 대답해준다.★

# 비교연산자
# 크다(>), 작다(<), 크거나 같다(>=), 작거나 같다(<=), 같지 않다(!=), 같다(==)
# ★비교연산자의 결과는 값이 아닌 Boolean으로 참(True)과 거짓(False)로 출력된다.
3>4   #False
3<4   #True
3==4  #False
3!=4  #True
# 비교연산자의 결과 Boolean의 결과 참, 거짓은 후에 나오는 '조건문, 반복문, 함수'에서 활용된다.


# 복합 대입 연산자
a = 3
a = a + 2 #오른쪽에 있는 게 먼저 연산이 되어서 왼쪽으로 들어간다고 생각하면 된다.
print(a)

a=3
a+=2
print(a)


# 문자열(String)
# 파이썬은 따옴표 '' 와 쌍따옴표 "" 둘다 사용 가능하다. 하지만 쌍으로 사용해야 한다.
# 변수 리셋하려면 오른쪽 Variable explorer에서 전부 드래그해서 delete해 줘도 되고, 아래 콘솔에서 restart kernel 눌러도 된다.
a = 'thank'
b = "you"
# 따옴표 하나와 쌍따옴표 하나로는 안 된다. c = 'thank"


# 따옴표 3개씩으로 둘러싸면 장문의 문자열, 줄바꿈도 쉽다.★
d = """t
h
a
n
k
s
"""
#"""가 있는 줄부터 """가 있는 줄까지 출력된다.
#따라서 t h a n k s _ 로 공백까지 출력된다. (공백까지 포함하여 d가 된다.)

# e ="이세인이 말했습니다. "안녕하세요" " 실행 안 된다.
# 위와 같이 string 안에 따옴표를 넣고 싶을 때에도★
e = """이세인이 말했습니다. "안녕하세요" """ 


# 문자열끼리의 합
a + b  #'thankyou'
a + " " + b  #안에 빈칸 넣어주고 싶으면(띄어쓰기해 주려면) " "을 써준다. #빈칸이 출력된다. #'thank you'


# 문자열에 숫자를 곱하면 그 숫자만큼 반복
a * 2


# 문자열에 변수를 사용하는 방법은 .format()을 활용하는 것이다.★
# 사용법 - 문자열 안의 "{}"가 변수인 것이고, string 마지막에 .format()으로 괄호안에 변수를 넣어준다.
# "{}".format(변수)

a = '이세인'
name = 'a' #문자열 형태를 가진 변수 a를 문자열 형태로 넣고 싶었지만 그냥 문자 a가 들어가졌다. name1에 '이세인'이 아닌 'a'가 들어가진다. 
name = "{}".format(a) #★ #변수를 문자열 형태의 값을 갖고 있는 그대로 문자열로 넣고 싶다면

name1 = '이세인'
email = 'lseinuu@gmail.com'
print("{}의 이메일 주소는 {} 입니다.".format(name1,email)) #★
#string안에 string형태의 값을 가진 변수를 넣어주고 싶을 때 {}와 .format()을 사용한다.


# 문자열(String)관련 주요 메소드
# split : 특정 문자 또는 빈칸으로 쪼개준다.
# ★결과는 리스트(list)로 나오는데 다음 강의에서 배운다.
s = "2021-06-01"
result = s.split('-')
print(result)         #['2021', '06', '01']

s = "안녕하세요. 제 이름은 이세인 입니다."
result = s.split(' ') # 빈칸으로 쪼갠다.
print(result)         #['안녕하세요.', '제', '이름은', '이세인', '입니다.']


# join : split와 반대로 메소드로 생각할 수 있다.★
# 사용 방법 - "리스트를 join시키면서 넣고 싶은 문자열".join(리스트 or 튜플)

result2 = ' '.join(result) # 빈칸을 활용하여 단어들로 구성된 result(리스트형)을 문자열(string)으로 변환
#안녕하세요. 제 이름은 이세인 입니다.


# upper() : 모두 대문자로
email.upper()
# lower() : 모두 소문자로
email.lower()
# capitalize() : 문자열의 첫 글자만 대문자, 나머지는 소문자
email.capitalize()  #'Lseinuu@gmail.com'


# 어떤 메소드는 소괄호 안에 넣고 어떤 메소드는 아닌 건 오픈소스 개발자들이 만들 때 정한 방식이기 때문에 규칙은 없다.

ex = s.center(50) #50칸 만큼 양쪽에 공간을 둔 것
ex_1 = s.center(50,'*') #양쪽에 50칸 만큼 *로 채워주겠다
ex_2 = s.center(50,'/')

s.count('이세인') #'이세인'이라는 문자가 몇 개가 있는 지
s.find('이세인') #'이세인'이라는 문자가 몇 번째 칸에 있는 가

ex.strip() #양쪽에 빈 공간을 없애는 것
ex_1.strip('*') #양쪽에 *을 다 없애준다.


"asdf123".isalnum()

"aaaaa".isalpha()

"3123123123".isdecimal()
"1111".isdigit()

# 음수는?!
"-1111".isdecimal() # 숫자인가 하면 아니라고 한다. -가 문자로 들어가있는 의미여서

# 아래와 같은 함수를 만들어서 사용해볼 수 있다.
def is_decimal(data) :
    try :
        temporary = float(data)
        return True
    except :
        return False

is_decimal("-1111")
is_decimal("1111")


# 식별자 체크 : 식별자란 ? : 변수의 이름, 함수의 이름 등등으로 사용할 수 있는 지 없는 지 확인
"a".isidentifier()
# 어렵게 생각하지 말고 변수에는 무조건 문자로 시작, 빈칸이 없어야 한다!!
"31".isidentifier()
"31a".isidentifier()
"a31".isidentifier()
"a a".isidentifier()
"a_a".isidentifier()


"3 \n dd".isprintable() #\n는 한 줄 띄는 거라서 보여질 수가 없는 거기에 false 나옴
print("3 \n dd")

" ".isspace() #빈칸 있는 지 없는 지
print("")
print(" ")

a = ""
b = " "
# 둘의 차이는 ?!
len(a)
len(b)




#과제(1)
# x = 5.0, y = 3을 입력하고, 결과창으로 "x + y = 8.0 입니다"를 출력하는 함수 작성
x = 5.0
y = 3
print("x + y = {} 입니다".format(x+y))

def add(x,y) :
        temp1 = float(x)
        temp2 = float(y)
        print("x + y = {} 입니다".format(temp1+temp2))
add(x,y)


# 답안지
print(""" x + y = {} 입니다""".format(x+y))


#과제(2)
# x = "than3k"
# y = "yo97u"
# x와 y를 위와 같이 선언한 후에, 강의에서 학습한 함수를 사용하여 "thank you"를 출력

x = "than3k"
y = "yo97u"
x = x.replace('3','')
y = y.replace('97','')
print(x + (' ')+ y)

# 답안지
print(x.replace('3','') + " " +y.replace('97',''))
