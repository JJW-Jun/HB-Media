# 돈(money), 동전의 갯수(count)
money, count = 1260, 0


# 동전의 종류
money_list = [500, 100, 50, 10]


# 현재 가진 돈을 동전별로 나눈 몫/나머지. 가장 큰수로 나눈 몫을 기준으로 count를 세면 최소한의 동전으로 값을 만들 수 있다.
for coin in money_list :
    count += money//coin
    money %= coin
