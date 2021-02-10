from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(1, M+1) :
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [-1]*(N+1)
distance[X] = 0

q = deque([X])
while q :
    now = q.popleft()
    for next in graph[now] :
        if distance[i] == -1 :
            distance[next] = distance[now] + 1
            q.append(next)