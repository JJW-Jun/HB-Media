# 돈(money), 동전의 갯수(count)
money, count = 1260, 0

# 동전의 종류
money_list = [500, 100, 50, 10]


for coin in money_list :
    # 현재 가진 돈을 동전별로 나눈 몫/나머지
    count += money//coin
    money %= coin
