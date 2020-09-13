이것이 코딩테스트다.
def location(number) :
    a, b = 1, 1
    for i in range(len(number)) :
        if number[i] == "R" :
            if b == 5 :
                pass
            else :
                b+=1

        if number[i] == "L" :
            if b == 1 :
                pass
            else :
                b-=1
        if number[i] == "U" :
            if a == 1 :
                pass
            else :
                a-=1

        if number[i] == "D" :
            if a == 5:
                pass
            else :
                a += 1

    return a, b

print(location(["R", "R", "R", "R", "D", "D"]) )






# def solution(s):
#     answers = re.findall(r'[a-z]+|[A-Z]+', s)
#     # answers = sorted(s, key=lambda x: (sorted(x)))
#     print(answers)
#
#     # answer, count = '', 0
#     # while count < len(answers) :
#     #     answer = answer + answers[count]
#     #     count += 1
#     return answers
#
# s = 'Zcbcdefg'
# print(solution(s))

# a = ['a', 'b', 'c','d']
# sum, count = '', 0
# while count < len(a) :
#     sum = sum + a[count]
#     print(a[count], '가 더해졌습니다')
#     count += 1
# print(sum)


# for i in rnage(len(s)) :
#     sorted(s, lambda s:s.lower())
# print(solution(b))


# def solution(s) :
#     if len(s) % 2 != 0 :
#         answer = s[int((len(s)-1) /2)]
#         return answer
#     else :
#         answer = s[int((len(s)/2 -1)):int((len(s)/2+1))]
#         return answer
#
# print(solution('banana'))


# if a > b :
#     a, b = b, a
#     if (b-a+1)/2 == 0 :
#         (a+b)*((b-a)/2)
#     else :
#         ((a+b)*((b-a)/2))-(a+b)/2
#
#
# elif a == b :
#     return a





