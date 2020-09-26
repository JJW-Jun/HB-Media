# Solution 01 : Greedy
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




# Solution 02 : 
n, plans = int(input()), input().split()
(x, y) = (1, 1)

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans :
    print('plan값 확인 : ', plan)
    for i in range(len(move)) :

        print('i값 확인 : ', i)
        if plan == move[i] :
            nx = x + dx[i]
            ny = y + dy[i]
            print('nx, ny값 확인 : ', (nx, ny))
    if nx < 1 or ny < 1 or nx > n or ny > n :
        print(nx, ny, '오류 발생')
        continue

    x, y = nx, ny
