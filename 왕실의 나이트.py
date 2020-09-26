input_data = input()
row, column = int(input_data[1]), int(ord(input_data[0])-int(ord('a')+1))

# Eight directions the Knight can move on.
steps = [(-2, -1), (1, -2), (2, -1), (2,1), (1, 2), (-1, 2), (-2, 1)]

# Check to see if the knight can move to each position.
count = 0
for step in steps :
    next_row, next_column = row+step[0], column+step[1]
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8 :
        count += 1