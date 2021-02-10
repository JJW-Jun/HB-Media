# 풀이법1
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b) :
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b : parent[b]=a
    else : parent[a]=b


n, m = map(int, input().split())
parent = [0]*n+1


for i in range(n+1):parent[i] = i
for i in range(m) :
    x, a, b = map(int, input().split())
    if x == 0 : union_parent(parent, a, b)
    if x == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :print("Yes")
        else : print("No")


# 풀이법2
def lstAdd(lst, a, b) :
    index_a, index_b = 0, 0
    if a==b : return lst
    for i in range(len(lst)) :
        if a in lst[i] : index_a = i
        if b in lst[i] : index_b = i
    lst[index_a].extend(lst[index_b])
    del lst[index_b]
    return lst


def lstCheck(lst, a, b) :
    for i in range(len(lst)) :
        if (a in lst[i]) & (b in lst[i]) :
            return "Yes"
    return 'No'


N, M = map(int, input().split())
lst = [[i] for i in range(N+1)]
for i in range(M) :
    x, a, b = map(int, input().split())
    if x == 0: print(lstAdd(lst, a, b))
    else : print(lstCheck(lst, a, b))



# 출처 : 이것이 코딩테스트다 p298