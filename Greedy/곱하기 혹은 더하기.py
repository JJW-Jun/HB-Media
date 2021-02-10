def solution(lst) :
    # 초기 합의 값을 0으로 설정
    sum_ = 0

    # 왼쪽부터 하나씩 수를 체크해서 검사
    for i in range(len(lst)):
        # 만약 이전까지 합이 0이라면 더해준다.
        if sum_ == 0:
            sum_ += int(lst[i])

        # 이전까지 합이 0이 아닌 경우
        else:
            # 각 항이 0 혹은 1, 직전까지의 합이 1이었을 경우 곱해주는 것 보다 더하는 것이 결과가 더 크게나온다.
            if (int(lst[i]) == 0) or (int(lst[i]) == 1)  or (sum_ == 1) :
                sum_ += int(lst[i])

            # 그 외는 다 곱해준다.
            else:
                sum_ *= int(lst[i])

    return sum_

lst = input()