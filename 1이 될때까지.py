# 두 문자 입력받기
N, K = map(int, input().split())
count = 0

# 1일 경우 종료하는 반복문
while N != 1 :
    if N % K == 0 :
        count += 1
        N /=K

    else :
        count += 1
        N += -1