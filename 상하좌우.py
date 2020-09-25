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
