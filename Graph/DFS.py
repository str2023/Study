# A 컨셉
# 1. 루트 노드를 '스택'에 넣고 방문 처리를 한다.
# 2. 스택의 최상단 노드와 인접한 노드 중에서 방문하지 않은 노드가 있다면 가장 작은 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 노드가 없다면 최상단 노드를 꺼낸다.
# 3. 스택이 빌 때까지 2번을 반복한다.
def dfsA_recursion(visited, node, graph):  # A컨셉의 재귀함수 방식
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            dfsA_recursion(visited, i, graph)

def dfsA_iteration(visited, start, graph):  # A컨셉의 반복문 방식
    visited[start] = True
    stack = [start]         # 1번 수행
    print(start, end=' ')
    while stack:    # 3번 스택이 빌 때까지 수행
        for i in graph[stack[-1]]:  # 스택의 최상단 노드와 인접한 노드 순회
            if not visited[i]:      # 그 노드를 방문하지 않았다면,
                stack.append(i)     # 스택에 넣고
                visited[i] = True   # 방문처리
                print(i, end=' ')            # (스택에 넣는 순서가 탐색 순서)
                break               # 다시 스택의 최상단부터 탐색
            if i == graph[stack[-1]][-1]:
                stack.pop()         # 방문하지 않은 노드가 없다면 최상단 노드를 꺼낸다.

# B 컨셉
# 1. 루트 노드를 '스택'에 넣고 방문 처리를 한다.
# 2. 스택의 최상단 노드를 꺼내고 그와 인접한 노드 중 방문하지 않은 노드를 '큰' 순서대로 전부 스택에 넣으며 방문 처리를 한다.
# 3. 스택이 빌 때까지 2번을 반복한다.

def dfsB(visited, start, graph):  # B컨셉
    stack = [start]
    visited[start] = True   # 1번 수행

    while stack:    # 3번 스택이 빌 때까지 수행
        node = stack.pop()              # 스택의 최상단 노드를 꺼내고
        print(node, end=" ")
        for i in reversed(graph[node]): # 인접한 노드 중 큰 순서대로,
            if not visited[i]:          # 방문하지 않았다면,
                stack.append(i)         # 스택에 넣으며,
                visited[i] = True       # 방문처리


graph = [   # 그래프는 인접 노드의 2차원 배열로 구현.
    [],     # 0번째 인덱스는 빈칸으로 하는 것이 인덱스 = 노드가 되므로 코드 작성이 편하다.
    [2, 5],
    [1, 3, 4],
    [2, 6],
    [2, 5],
    [1, 4, 7, 8, 9],
    [3, 7],
    [5, 6],
    [5],
    [5],
]
visited = [False] * 10  # 방문체크 리스트.
dfsB(visited, 1, graph)