lst = []
def pureFunction (n) :
    for i in range(n) :
        if i % 2 == 0 :
            lst.append(i)
    return "Complete"

print(pureFunction(10))
print(lst)


x = 0
def f() :
    if x==0 :
        print("zero")
    return x

print(f())
# print(pureFunction(1, 2))
# print(count)

# z = (print(True) if count == 1 else count += 1)
# print(z)
