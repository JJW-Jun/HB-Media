# 아스키코드는 숫자, 문자가 순서대로 증가, 감소하기 때문에 이를 활용해 x, y좌표를 낼 수 있다.
input_data = input()
row, column = int(input_data[1]), int(ord(input_data[0])-int(ord('a')+1))

# 말이 이동할 수 있는 8가지 방향의 좌표값을 나타낸 리스트.
steps = [(-2, -1), (1, -2), (2, -1), (2,1), (1, 2), (-1, 2), (-2, 1)]

# if문을 활용해 말이 움직일 수 있는지 체크.
count = 0
for step in steps :
    next_row, next_column = row+step[0], column+step[1]
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8 :
        count += 1
