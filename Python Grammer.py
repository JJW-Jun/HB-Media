# 2020.06 ~ 현재.
# 코딩테스트를 위해 필요한 내용을 정리/요약한 문서입니다. 필요한 내용은 ctrl + f로 찾으시면 됩니다.
# '이것이 코딩테스트다' '파이썬 코딩도장'을 위주로 정리했습니다.



## 사칙연산
# 나눗셈 : / , 실수(float) type으로 출력된다.
print(5/2)

# 버림 나눗셈(floor division) : // (나눗셈 후 소숫점을 버린다), 정수(int) type으로 출력된다.
print(5//2)

# 나머지 구하는 연산자 : %
print(5%2)

# 제곱 연산자 : **
print(2**2)

# 몫과 나머지 함께 구하기 : divmod(x, y) - tuple형태로 나온다
print(divmod(5, 2))

# 실수(float)과 정수(int) : 실수와 정수를 함께 계산하면 표현 범위가 넓은 실수로 계산된다.


## 2진수, 8진수, 16진수
# 2진수 : 숫자 앞에 0b를 붙이며 0과 1을 사용한다.
print(0b110)

# 8진수 : 숫자 앞에 0o를 붙이며 0부터 7까지를 사용한다.
print(0o110)

# 16진수 : 숫자 앞에 0x또는 0X를 붙이며 0부터 9까지, A(a)부터 F(f)까지 사용한다.
print(0x111)





## print 함수 : script file
# 파이썬 셸은 결과를 즉시 보는 용도라서 값 또는 계산식만 넣어도 결과가 출력된다. 하지만 스크립트 파일에서는 반드시 print 함수를 사용해야 한다.
# print() : 출력함수.
print('Hellow world')


# print(sep) : ,를 기준으로 나누어 준다.
# a = 1, 2라고 선언하면 tuple형태가 되듯 스트링형, 리스트형은 sep으로 구분안된다
print('2019', '08', '09', sep='-')
print('jjw9w1', 'google.com', sep='@')



# end 옵션 : print() 함수는 원래는 한 줄을 내려가지만 end=''를 이용해 customize가 가능하다.
print('welcome to the', end='')
print('new world', end='')
print('')



# format 함수
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a}, {b}'.format(a='You', b='Me'))



# round 함수 : 소숫점 n자리 까지 표현
# round(숫자, n자리)
# "%.2f   >>> print("{0:.2f}".format(a))
#   13.95
#   >>> print("{0:.2f}".format(round(a,2)))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d"%('JunWoo', 7))



# 정수, 소수 표현
print("Test1 : %5d, Price : %4.2f"%(776, 6534.333))
print("test1 : {0:5d}, price : {1: 4.2f}".format(776, 6532.3333))
print("test1 : {a:5d}, price:{b:4.2f}".format(a=776, b=6532.3333))



# escape 코드 : 출력물을 보기 좋게 정렬하기 위한 용도
print('"you"')
print('\'you\'')
print(""'you'"")
print('\\you\\')
print('\t\t\ttest')
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab \tTat\tTab"
print(escape_str2)



###
import this
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)



# for 반복문
for i in range(1, 10) :
    for j in range(1, 10) :
        print('%d * %d = '%(i,j), i*j)



## 변수 : 값을 '할당'하는 것  ex) x = 10 은 10을 x에 할당하겠다는 의미.
# 영문, 한글 문자와 숫자를 사용할 수 있다. 이때 대소문자를 구분한다.
# 문자부터 시작해야 하며 숫자부터 시작하면 안 된다.
# _(밑줄 문자)로 시작할 수 있다.
# 특수문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없다.
# 파이썬 키워드(if, for, while, and, or 등)는 사용할 수 없다. 만약 사용해야할 경우 for_와 같이 사용한다.
이름 = '좋은사람'
print(이름)


# 변수 여러개를 한 번에 선언할 수 있다. 여러개를 묶어서 출력할 경우 tuple형태로 나온다.
x, y, z = 10, 20, 30
a = x, y, z
print(x, y, z)
print(a)


# 여러개의 변수 값이 같을 경우 등호를 사용한다.
a = b = c = 10
print(a)


# 두 변수값을 바꿀 때 : 자리를 바꾼다.
x, y = 10, 20
x, y = y, x
print(x)


# 빈 변수 만들기 : None(다른 언어에서는 null이라고 한다)
x = None
print(x)


# 프롬프트(prompt) : 사용자에게 입력받는 값의 용도를 미리 알려줄 때 사용된다(파이썬 프롬프트 >>>와 같은 의미)


# 여러개의 변수 입력받기
a, b = input('문자를 두 개 입력하세요').split(',') # ex)'Hello Python'을 입력했을 경우 공백을 기준으로 a, b에 할당된다
print(a, b)
print(a)

x, y, z = input('숫자를 입력해주세요').split(',')
x, y, z = int(a), int(b), int(c) # 이것을 지정해주지 않으면 str으로 들어온다(기본 셋팅)
print(x+y+y)






# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)



# 문자열 연산 / 슬라이싱(slicing)
a = 'Niceman'
b = 'orange'

print('a' in a)
print(a.islower())
print(a.endswith('n'))
print(a.capitalize())
print(a.replace('Nice', 'good'))
print(list(reversed(a)))



print(b[1:-2])
print(b[::-1])



# list 수정 / 삭제 : del
c = [1, 2, 3, 4, 5, 6]
c[1] = ['a', 'b', 'c']

del c[1]
print(c)



# 리스트 함수
y = [5, 2, 3, 1, 4]



# append 함수 : 추가
y.append(7)
print(y)



# sort 함수 : 정렬
y.sort()
print(y)



# reverse 함수 : 순서 뒤집기
y.reverse()
print(y)



# insert 함수 : list 추가
y.insert(2, 7)
print(y)



# remove 함수 : list 제거
y.remove(7)
print(y)



# pop 함수 : 마지막에 들어간 원소를 꺼낸 후 삭제한다.
y.pop()
print(y)



# extend 함수 : 함수 추가 / 리스트 채로 추가한다.
ex = [88, 77]
y.extend(ex)
print(y)



# tuple : 원소를 추가 / 삭제할 수 없다.
a = ()
b = (1, )
c = (1, 2, 3, 4)



# count 함수 : 해당 인자가 몇 번 사용 되었는지 세기 위한 함수 / list와 tuple은 사용가능. dic는 사용불가.
z = (5, 2, 1, 3, 4)
print(z.count(1))



# index 함수 : 몇 번째에 그 항이 있는지 찾기 위한 함수 / list와 tuple은 사용가능. dic는 사용불가.
z = (5, 2, 1, 3, 4)
print(z.index(5))



# dictionary : key는 중복하여 사용 할 수 없다.
a = {'name' : 'jun', 'num' : '010-4059-3401', 'birth' : '911023' }
b = {'arr' : [1, 2, 3, 4, 5]}

print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(b['arr'][1:3])



# dictionary 추가 : 직접추가 / update 함수
a['address'] = 'Seoul'
a['rank'] = '1st'
a['rank2'] = (1, 2, 3)
a.update({'test':'math'})



# key : 해당 dictionary의 key 확인 / ex) a.keys()
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])



# value : 해당 dictionary의 value 확인 / ex) a.values()
print(a.values())



# items : 해당 dictionary의 key, value 확인 / ex) a.items()
print(a.items())
print(list(a.items()))



# a in b : key가 원소로 있는지 확인 / True or False로 return. dictionary는 key를 기준으로 검색한다.
a = [1, 'rank', 3, 5]
print(1 in a)
print('rank' in a)



# 집합(Set) : 순서 / 중복을 허용하지 않는다. 집합을 리스트로 나타내기 위해서는 set([]) 형태로 표현해야 한다.
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)



# 형태 변환 : ex)list -> tuple / tuple -> list
t = tuple(b)
l = list(b)



# 집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])



# 교집합
print(s1.intersection(s2))
print(s1 & s2)



# 합집합
print(s1|s2)
print(s1.union(s2))



# 합 집합
print(s1-s2)
print(s1.difference(s2))



# 집합의 원소 추가, 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(7)

s3.remove(15)
print(type(s3))




# 연습문제
# 1.print함수를 사용해서 다음과 같이 출력해보세요 : apple;orange;banana;lemon
print('apple', 'orange', 'lemon', sep=';')



# 2.다음 문자열을 거꾸로 출력해보세요 : 'Start'
q2 = 'start'
print(reversed(q2))
print(q2[::-1])



# 3.다음 문자열에서 '-'를 제거 후 출력하세요 : '010-7777-7777'
q3 = '010-7777-7777'
print(q3[0:3]+q3[4:8]+q3[9:13])
print(q3.replace('-',''))



# 4. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMans"
q4 = 'NiceMans'
print(q4.lower())
print(q4.upper())



# 5. 다음 리스트에서 'Apple'항목만 삭제하세요. : ['Banana', 'Apple', 'Orange']
q5 = ['Banana', 'Apple', 'Orange']
q5.remove('Apple')



# if문 : 흐름제어(제어문)
print(type(True))
print(type(False))



# if 문에서 True/False 구분
# 참 : '내용', [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False



# 논리 연산자(and / or / not)
print('ex1: ', 5+10 >0 and not 7 +3 == 10)



# 다중조건문 : if 중첩문
num = 90
if num >= 90 :
    print('num 등급 A', num)

elif num >= 80 :
    print('num 등급 B', num)

elif num >= 70 :
    print('num 등급 C', num)

else :
    print('꽝')



# 중첩 조건문 : if문 안의 if문
age = 27
height = 175
if age >= 20 :
    if  height >= 170 :
        print('A지망 지원 가능')

    elif height >= 160 :
        print('B지망 지원 가능')

    else :
        print('지원 불가')

else :
    print('20세 이상 지원 가능')



# 기본 반복문 : for, while
v1 = 1
while v1 < 11 :
    print('v1 is :', v1)
    v1 += 1

for v2 in range(10) :
    print('v2 is :', v2)



# 예시. 1부터 100까지의 합
sum = 0
num = 0
while num <= 100 :
    sum += num
    num += 1
print('합계는 '+str(sum)+' 입니다')



# 1부터 100까지의 짝수의 합을 구하세요
sum = 0
num = 0
while num <= 100 :
    if num %2 == 0 :
        num

    else :
        num == 0

    sum += num
    num += 1

print('합계는 '+str(sum)+' 입니다!')



# 시퀀스 자료형 : 순서가 있는 자료형의 반복 / str, list, tuple, set, dictionary
# iterable : range, reversed, enumerate, filter, map, zip 함수
names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']
for name in names :
    print('Your are :', name, '입니다')

word = 'dreams'
for s in word :
    print('word is :', s)



# dictionary : key와 value로 구성
my_info = {'name' : 'Jung', 'age' : 30, 'city':'Seoul'}



# 기본 값 : key
for key in my_info :
    print(key)

# key
for key in my_info.keys() :
    print(key)

# value
for key in my_info.values() :
    print(key)

# key & value
for key, value in my_info.items() :
    print(key, value)



# isupper(대문자) / islower(소문자) :
name = 'JunWoooooo'
for n in name :
    if n.isupper() :
        print(n.lower())
    else :
        print(n.upper())



# break : 반복문 탈출
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 43, 38]
for num in numbers :
    if num == 39 :
        print('found :', 33)
        break

    else :
        print('not found :', 33)

# 마지막에 else가 있으면 for 문에서 break가 걸리지 않았을 때
else :
    print('Not found 33.......')



# continue : 계속문
list = ['1', 2, 5, True, 4.3, complex(4)]
for v in list :
    if type(v) is float :
        continue
        print('type() :', type(v))



## 문제 1번 ##
## 아래 Dictionary에서 '가을'에 해당하는 과일을 출력하세요 ##
q1 = {'봄':'딸기', '여름':'토마토', '가을':'사과'}
print(q1['가을'])


# 문제 2번
# 아래 Dictionary에서 '사과'가 포함되었는지 확인하세요.
q2 = {'봄':'딸기','여름':'토마토', '가을':'사과'}
print(len(q2))

for k, v in q2.items() :
    if v == '사과' :
        print(k, v)


## 문제4. 다음 세 개의 숫자 중 가장 큰 수를 출력하세요(if문 사용할 것) ##
a, b, c = 12, 6, 18
best = a

if b > a :
    best = b

if c > b :
    best = c
print('best: ', best)


# 문제5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요(1, 3은 남자, 2,4는 여자)
s = '911023-1123312'
if int(s[7]) % 2 == 0 :
    print('남자입니다.')
else :
    print('여자입니다.')


# 문제6. 다음 리스트 중에서 '정'글자를 제외하고 출력하세요.
q6 = ['갑', '을', '병', '정']
for i in q6 :
    if i == '정' :
        q6.remove('정')
        continue
    else :
        print(i, end='')



print(end = ' ')

# 문제9. 아래 리스트 항목 중에서 소문자만 출력하세요
q9 = ['A', 'B', 'c', 'D', 'e', 'f']
for i in q9 :
    if i.isupper() :
        print(i, end=' ')

# 문제 10. 아래 리스트 항목 중에서 소문자는 대문자로, 대문자는 소문자로 출력하세요.,
q10 = ['A', 'B', 'c', 'D', 'e', 'f']

for i in q10 :
    if i.isupper() :
        print(i.lower())
    else :
        print(i.upper())




# list comprehension : 추가 할 변수 x지정 / x in range(1, 100) / 조건문 : ex) if, !=
numbers = [x for x in range(1, 101)]
print(numbers)



# 추가 연습문제 1번
q6 = [x for x in q6 if x != '정']
print(q6)

# 추가 연습문제 2번
q6 = [x for x in range(1, 101) if x%2 != 0]
print(q6)



### 람다 함수 ###


#######################################################################################################################
######################################################### 함수 #########################################################
#######################################################################################################################
""" 
1. 주어진 입력(input)에 대해서 출력(output)을 전달하는 과정
2. 입력값 argument, parameter / 몸 가진다.
3. body는 함수의 몸통
4. Python의 경우 타입 명시가 없기 때문에 함수 생성 시 의도된 파라미터의 타입에 맞게 입력을 전달하는 것이 중요하다.
5. return : 반환값. 함수를 호출해서 결과를 알려준다. 이 값을 변수에 저장할 수 있다. 
"""







# def print_numbers(a, *args) :
#     print(a)
#     print(*args)
#
#
# print(print_numbers(1))
# print(print_numbers(1, 10, 20))
# print(print_numbers(*[10, 20, 30]))
#
#
# print('-'*80)
#
#
# def print_number(a, b,c) :
#     print(a)
#     print(b)
#     print(c)



# def personal_info(name, age, address) :
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소:', address)
#
# personal_info('정준우', 30, '서울시 신림동')


# test2

def personal_info(name, age, address) :
    print('이름: ', name)
    print('나이: ', age)
    print('주소:', address)


# key 값이 반드시 같아야 한다.
x = {'name':'홍길동', 'address':'서울시 중구', 'age':29}
print(personal_info(*x))
print(personal_info(**x))


# 위에서 특정 값을 명시 했어도 input한 값이 나온다.
def add(x, y, z=5) :
    return x+y+z

a = add(5,1,10)
print(a)


# doc 스트링 / help(객체) : 주석
def add(a, b) :
    """a와 b를 입력 받아서 더해주는 함수입니다"""
    return a + b
print(add.__doc__)
print(help(add))


# 매개변수는 없고 반환값만 있는 함수
def one() :
    return 1

print(one())



# 문자끼리의 덧셈은 가능하지만 뺼셈은 불가능하다.
a = '마'
b = '늘'
print(a+b)


# 스택 다이어그램(stack diagram) :
# 프레임 : 메모리에서 함수와 함수에 속한 변수가 저장되는 독립적인 공간
# 전역 프레임 : 파이썬 스크립트 전체에 접근할 수 있다.
# 디폴트 파라미터 값(Default parameter value)는 뒤에서 부터 와야한다.
def test(a, b=1, c=3) :
    return a, b, c

print(test(1, 4, 3))


# 키워드 파라미터(Keyword parameter) : 파라미터(입력 값)의 이름을 명시한다.
def test(x, y, z) :
    a = x+y+z
    return a

print(test(x=10, y=20, z=3))


# return : 함수 값을 반환. 단순히 return만 존재하면 None값을 반환한다. return 옆에 값, 수식이 있다면 해당 값을 호출자(caller)에 반환(전달)
def multiply(x, y) :
    if x > 10 :
        return x*y

    return (x+2)*y

print(multiply(5,2))



# None 반환 : return 값이 없거나 혹은 조건함수
def weird_multiply(x,y) :
    if x>10 :
        return x*y

print(weird_multiply(2,5))



# multiple return : 복수 값 반환
def add_mul(x, y) :
    s = x+y
    m = x*y
    return s, m

print(add_mul(20,3))



# 값 여러 개를 직접 반환하기 : return 1,2 와 return(1, 2)는 의미가 같다.
def one_two() :
    return 1, 2

print(one_two())



# return에서 리스트를 직접 반환해도 된다. 반환값을 변수 여러 개에 저장할 수 있다.
def one_two() :
    return [1, 2]
x, y = one_two()

print(x, y)



# 변수의 범위 : 변수가 참조 가능한 코드상의 범위를 명시한다. 함수 내에서만 유의하다.
# 지역변수(local variable) : 특정 코드블록에서 선언 된 함수.
# 전역변수(global varibable) : 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수.
# 같은 이름의 지역변수와 전역변수가 존재할 경우 지역변수의 우선순위가 더 높다.


num1 = 10
num2 = 30

def test(num1, num2) :
    num3 = 40    # 함수 밖에서 지역변수를 print하면 오류가 난다.
    print(num1, num2)
    return num1+num2

print((test(30,40)))
print(num1, num2)


# 언패킹(unpacking) : 리스트의 포장을 푼다. 변수를 몇 개 넣어도 상관 없다.
# variable length argument(가변인자) : 여러개의 변수를 받을 수 있으며 tuple형태로 출력된다.
# 가변길이 함수의 대표적인 예 : 문자열 포맷 함수(format 함수)
# 여러가지 값과 포맷을 이용하여 문자열을 정의할 수 있는 함수
# placeholder를 문자열 내에 이치시킨 후 해당 위치에 format함수 값을 전달하여 문자열 구성
def firstname_lastname(*name) :
    for i in name :
        print('{} {}'.format(i[0], i[1:3]), end=' ')
        # print(type(firstname_lastname('정준우', '정가은', '금정원'), name))

print(firstname_lastname('정준우', '정가은', '금정원'))


def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)

number = [1,2,3]
print(print_numbers(*number))


# keyword parameter : **가 붙은 경우 키워드 파라미터로 인식(dictionary), kwargs : xx 형태로 출력 가능하다
# 함수 호출 시 파라미터의 이름과 값을 함께 전달 가능
def introduce(**kwargs) :
    for key, value in x.items() :
        print('검색하신 {}는 {}입니다'.format(key, value))

# print(introduce('내 몸무게', 90))



# lambda 함수 : return 키워드 없이 바로 사용한다.
# lambda 자체가 함수라 함수처럼 바로 사용할 수 있다.
square = lambda x : x**2
print(type(square))
print(square(5))


add2 = lambda x,y : x+y
add2(10, 20)
print(add(10, 20))



# sort 함수 : 정렬
# key로 특정 함수를 받을 수 있다.
def str_len(s) :
    return len(s)

strings = ['bob', 'sophie', 'Ki-hoon', 'air']
strings.sort(key=str_len)
print(strings)


# filter(함수, 리스트) : 특정한 값을 걸러주는 역할을 해주는 함수
# lambda가 유용하게 사용되는 3가지 대표적 함수
# 함수형 프로그래밍의 기본 요소이기도 함

# 예제1
nums = [1, 2, 3, 6, 8, 9]

def even(n) :
    return n % 2 ==0

print(list(filter(even, nums)))



# 예제2
result = []
for value in nums :
    if even(value) :
        result.append(value)
print(result)




# map함수
# 주어진 리스트가 있으면 함수를 적용해 처리해 주는 함수
###map(함수, 리스트)

map(lambda x:x**2, nums)
print(list(map(even, nums)))


# reduce : 2개의 결과를 받는다
import functools
#functools.reduce(함수, list)
a = list(range(1, 11))
num = functools.reduce(lambda x, y=x+y, a)
print(num)


# 주어진 숫자 리스트으 평균을 구하는 함수를 출력하시오
def mean(nums) :
    _sum = 0
    for i in nums :
        _sum += i
    return _sum / len(nums)

nums = [1, 3, 4, 5, 8, 40]
print(mean(nums))



# 소수 : 1과 자기 자신만을 약수로 가지는 수
# 합성수 :
# def know(number) :
#     numberz = int(input('숫자를 넣어주세요'))
#     if numberz > 3 :
#         for i in range(2, number) :
#             if numberz % i == 0 :
#                 print('소수가 아닙니다')
#                 return False
#             else :
#                 print('소수 입니다.')
#                 return True
#
#     elif numberz == 2 :
#         return print('소수입니다')
#         True
#
# print(know(17))




# class(클래스) : 속성(attribute)와 행동(method)를 가진다. / ex) a.append(5) # append라는 method를 이용해서 a에 attribute를 추가한다.
# object(객체)
# a = [1, 2, 3, 4]
class Person :
    pass

bob = Person()
cathy = Person()
a = list()
print(type(bob), type(a))



# 함수 정의
def hello(world) :
    print('Hello', world)

hello('Python!')
hello(7777)



# 예제1 : return 값이 존재하지 않는 경우
def hello(world) :
    print('Hello', world)

print(hello(world))



# 예제2 : return 값이 존재하는 경우
def hello_return(world) :
    val = 'Hello' + str(world)
    return val

str = hello_return('whatis!!!')
print(str)



# 다중 리턴 : 동시에 여러개의 값을 return / tuple형태(기본 설정)로 받는다.
def fun_mul(x) :
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = fun_mul(100)
print(val1, val2, val3)
type(val1)



# 예제3(데이터 타입 리턴)
def fun_mul2(x) :
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

list = fun_mul2(100)
print(list, type(list))



# 예제4 : *args, **kwargs : tuple은 index함수를 사용하지 못 한다.
def args_fun(*args) :
    print(args)
    for i,v in enumerate(args) :
        print(i, v)

print(args_fun('kim', 'jung'))



# kwargs(키워드 인자)
def kwargs_func(**kwargs) :
    print(kwargs)

kwargs_func(name1='Kim', name2='Park', name3 = 'Lee')
print(kwargs_func)



# 전체 혼합(arg1, arg2 : 필수 인자, 나머지 : 가변 인자) / 고도화된 함수
def example_mul(arg1, arg2, *args, **kwargs) :
    print(arg1, arg2, args, kwargs)

example_mul(10, 20, 'park','kim', age1=24, age2=35)



# 중첩함수(클로저) : 함수 안의 함수. 효율적 메모리 사용 가능.
def nested_func(num) :
    def func_in_func(num) :   #함수를 넘김. 변수를
        print(num)
    print('in func')
    func_in_func(num+10000)   # 여기서 실질적으로 실행

nested_func(10000)



# 인자(parameter)정의
def func_mul3(x : int) -> list :
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))


# ascending / descending


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 개체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 사용하지 않더라도 메모리를 할당한다
def mul_10(num : int) -> int :
    return num * 10

var_func = mul_10
print(var_func)



lambda_mul_10 = lambda num : num * 10
print(lambda_mul_10(10))



def  func_final(x, y, func) :
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)
print(func_final(10, 10 , lambda x : x * 10 ))



# 클래스(class) : 속성(attribute) / 메소드(method)로 구성 돼 있다.
# Self, 클래스, 인스턴스 변수
# 선언 : 첫 글자는 대문자로. 마찬가지로 단어와 단어가 연결될 때 대문자 / pass습관화

class UserInfo :
    def __init__(self, name):  # init은 클래스를 초기화
        self.name = name



    def user_info_p(self):
        print('Name :', self.name)

# class를 만들어서 할당은 한다. 하지만 각자 다르다
# user1 할당. 네임스페이스가 다르면 같지 않다.
user1 = UserInfo('Kim')
user1.user_info_p()
print(user1.name)

# user2 할당
user2 = UserInfo('Park')
user2.user_info_p()
print(user1.__dict__)
print(user2.__dict__)


# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용



# 예제2 : self으 ㅣ이해

class SelfTest :
    def function1() :
        print('function called')
    def function2(self) :
        print(id(self))
        print('function2 called')

# self가 없기 때문에 class에서 호출해야 한다. 누구의 함수인지모른다
self_test = SelfTest()
#self_test.function1()

# self인자가 있기 때문에 바로 호출할 수 있다.
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)



# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse :
    # 클래스 변수(self x)
    stock_num = 0
    def __init__(self, name) :
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self): # 종료될 떄 선언되는 함수
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

# 자기 name스페이스에 없으면 클래스로 간다. 거기도 없으면 에러가 난다.
print(user1.stock_num)
print(user2.stock_num)






# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능
# 상속을 통하면 코드를 재사용 할 수 있고 최소화할 수 있다. 복잡한 코드를 단순화 하기 위해서 사용한다.

class car :
    '''Parent Class'''
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self) :
        return 'Car Class "Show Method!"'

class BMW(car) :
    '''Sub Class'''
    def __init__(self, car_name, tp, color) :
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None :
        return 'Your Car Name : %s '% self.car_name


class Benz(car) :
    '''Sub Class'''
    def __init__(self, car_name, tp, color) :
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None :
        return 'Your Car Name : %s '% self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s' % self.car_name, self.type, self.color

# 일반 사용
model1 = BMW('520d', 'Sedan', 'Red')
print(model1.color)        # 부모로 부터 상속
print(model1.type)         # Super
print(model1.car_name)     # Sub
print(model1.show())       # Super
print(model1.show_model())  # Sub
print(model1.__dict__)


# Method Overiding(오버라이딩)
model2 = Benz('220d', 'Suv', 'Black')
print(model2.show())       # 부모에도 있고 자식에도 있다면 자식이 우선.



# Parent Method Call
model3 = Benz('350s', 'Sedan', 'Silver')
print(model3.show())

# 상속이 깊을 때 : Inheritance Info(상속 정보를 list형태로 반환)
print(BMW.mro())
print(Benz.mro())


# 다중 상속
class X(object) :
    pass

class Y() :
    pass

class Z() :
    pass

# X와 Y를 상속받겠다
class A(X, Y) :
    pass

class B(Y, Z) :
    pass

class M(B, A, Z) :
    pass

print(M.mro())
print(A.mro()) # depth가 복잡해질수록 코드가 알기 힘들어진다.



class Fibonacci :
    def __init__self(self, title = 'fibonacci'):
        self.title = title

    def fib(n) :
        a, b = 0, 1
        while a < n :
            print(a, end='')
            a, b = b, a+b

    def fib2(n) :
        result = []
        a, b = 0, 1
        while a < n :
            result.append(a)
            print(a, end='')
            a, b = b, a+b
        return result


def part1() :
    print('Im boy')



# from pkg.Fibonacci import Fibonacci
# 파일 읽기/쓰기
# 읽기 모드 : r / 쓰기 모드(기존 파일 삭제) : w / 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로 / . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

#
# # 예제1
# f = open('C:/Users/User/Desktop/김란이 주임님.txt', 'r', encoding='utf8')
# content = f.read()
# print(content)
# print(dir(f))
# #반드시 close리소스 반환
# f.close()
#
#
# # 예쩨2 : close생략 가능
# with open('C:/Users/User/Desktop/김란이 주임님.txt', 'r', encoding='utf8') as f :
#     c = f.read()
#     print(c)
#     # print(list(c))
#     # print(iter(c))
#
# print('-'*80)
# print('-'*80)
#
#
# # 예제3 : strip() 함수
# with open('C:/Users/User/Desktop/김란이 주임님.txt', 'r', encoding='utf8') as f :
#     for c in f :
#         print(c.strip())
#
#
# print('-'*80)
# print('-'*80)
#
# with open('C:/Users/User/Desktop/김란이 주임님.txt', 'r', encoding='utf8') as f :
#     content = f.read()
#     print('>', content)
#     content = f.read()      # 내용 없음
#     print('>', content)     # 한 번 읽고 끝까지 가서는 더 이상 오지 않는다.
#
#
# print('-'*80)
# print('-'*80)
# with open('C:/Users/User/Desktop/김란이 주임님.txt', 'r', encoding='utf8') as f :
#     line = f.readline()
#     while line :
#         print(line, end= '')
#         line = f.readline()
#
#
# 파이썬 예외처리의 이해 : 문법적으로는 에러가 없지만, 코드 실행(runtime)프로세스에서 발생하는 예외 처리도 중요하다.
# linter : 코드 스타일 / 문법 체크
# SyntaxError : 잘못된 문법
# print('tes)

# if True



# NameError : 참조변수 없음
# a = 10
# b = 15
# print(kk)
#
#
# # ZeroDivisionError : 0 나누기 에러
# # print(10/0)
#
#
# IndexError : index 범위 초과
# x = [10, 20, 30]
# print(x)
# print(x[3])



# KeyError : 해당 key 값이 없다. get 함수를 써주는 것이 좋다.
dic = {'name':'Kim', 'Age':33, 'City':'Seoul'}
# print(dic['hobby'])
print(dic.get('hobby'))



# AttributeError : 모듈 / 클래스에 있는 잘못된 속성 사용
import time
print(time.time())
# print(time.month())



# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)



# FileNotFoundError : 지정된 경로에서 파일을 찾을 수 없을 때.
# f = open('test.txt', 'r')



# TypeError : 타입이 달라서
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x+y)



# 예외 처리 : Error가 발생했을 경우 예외 처리
# try(에러가 발생할 가능성이 있는 코드 실행) / except(에러명) / else(에러가 발생하지 않았을 경우 실행) / finally(항상 실행)
name = ['Jun', 'Lee', 'Park']
try :
    z = 'Jun'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))

except ValueError :
    print('Not found it')

else :
    print('Ok! else!')



# 예제2번
name = ['Kim', 'Lee', 'Park']
try :
    z = 'Jung'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))

except :
    print('Not found it')

else :
    print('Ok! else!')



# 예제2번
name = ['Kim', 'Lee', 'Park']
try :
    z = 'Jung'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))

except :
    print('Not found it')

else :
    print('Ok! else!')

# 무조건적인 수행
finally :
    print('finally ok!')



# 예제4 : 예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try :
    print('Try')
finally :
    print('Ok! Finally!')



# 예제 5 :
name = ['Kim', 'Lee', 'Park']
try :
    z = 'Jung'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))

except ValueError :       # 예제를 정확히 알고 오류를 설정하는게 좋다
    print('Not found it - ValueError Error!')

except IndexError :
    print('Not found it - IndexError Error!')

except Exception :         # 위에서 부터 아래로 가서
    print('Not found it - Occurred Error!')

else :
    print('Ok! else!')

finally :
    print('finally ok!')



# # 예제 6
# # 예외 발생 : raise
# # raise 키워드로 예외 직접 발생
# try :
#     a = 'Kim'
#     if a == 'Gim' :
#         print('ok')
#     else :
#         raise ValueError
#
# except ValueError :
#     print('Problem occured')
#
# except Exception as f:
#     print(f)
#
# else :
#     print('ok')
#
#

# csv 파일 읽기/쓰기
import csv
# with open('C:/Users/User/Desktop/testtt.csv', 'r') as f :
#     reader = csv.reader(f)
#
#     # # Headr를 스킵할 때 사용한다.
#     # next(reader)
#
#     # 확인
#     print(reader)
#     print(type(reader))
#     print(type(reader))
#     print(dir(reader))
#     print()
#
#     for c in reader :
#         print(c)
#
#
#
# with open('C:/Users/User/Desktop/testtt.csv', 'r') as f:
#     reader = csv.reader(f, delimiter = '|')
#
#     # # Headr를 스킵할 때 사용한다.
#     # next(reader)
#
#     # 확인
#     print(reader)
#     print(type(reader))
#     print(type(reader))
#     print(dir(reader))
#     print()
#
#     for c in reader:
#         print(c)
#
#
# # 예제 3(Dict 변환)
# with open('C:/Users/User/Desktop/testtt.csv', 'r') as f:
#     reader = csv.DictReader(f)
#
#     for c in reader :
#         for k, v in c.items() :
#             print(k, v)
#         print('-----------------------')
#
#
# # 예제4
# # w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16,17,18]]
# # with open('C:/Users/User/Desktop/testtt.csv', 'w') as f :
# #     wt = csv.writer(f)
# #     for v, in w :
# #         wt.writerow(v)
#
#
# # 데이터 생성 및 삽입 (DB)
# import sqlite3
# import datetime
#
# print('sqlite3.version :', sqlite3.version)
# print('sqlite3.sqite_version:', sqlite3.sqlite_version)
#
# now = datetime.datetime.now()
# print('now :', now)
#
# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# print(nowDatetime)





# 삽입 날짜 생성
import sqlite3
import datetime

now = datetime.datetime.now()
print('now: ', now)



# 현재 날짜 출력
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)



# Version 체크
# print('sqlite3.version: ', sqlite3.version)
# print('sqlite3.sqite_version: ', sqlite3.sqlite_version)
#
#
#
# ##### DB 생성 & Auto Commit : Auto Commit은 그때그때 사용하겠다는 것(<->Rollback) #####
# conn = sqlite3.connect('C:/Users/User\Desktop/01. 파이썬기초핵심_강의코드/강의 코드/전체 예제 소스 - 파이썬 기초/resource/database.db',
#                        isolation_level = None)



# Cursor
# c = conn.cursor()
# print('Cursor Type: ', type(c))


# 테이브르 생성(Data Type : Text, Numeric, Real, Blob 등)
# c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)')


# # 데이터 삽입
# c.execute('INSERT INTO users VALUES(1, "Kim", "Kim@naver.com", "010-0000-0000", "www.naver.com", ?)', (nowDatetime, ))
# c.excute("INSERTINTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?)"(2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com'))
