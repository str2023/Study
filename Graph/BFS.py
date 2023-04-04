from collections import deque

# 1. 루트 노드를 '큐'에 넣고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내고 그와 인접한 노드 중 방문하지 않은 노드를 '작은' 순서대로 전부 큐에 넣으며 방문 처리를 한다.
# 3. 큐가 빌 때까지 2번을 반복한다.

def bfs(visited, start, graph): #visited:방문체크리스트, start:노드 인덱스, graph:그래프 구조
    queue = deque([start])
    visited[start] = True   # 1번 수행

    while queue:    # 3번 큐가 빌 때까지 수행
        v = queue.popleft()     # 2번 큐에서 노드를 꺼낸다
        print(v, end=' ')       # 탐색된 노드 출력
        for i in graph[v]:      # 인접 노드를 순회하며,
            if not visited[i]:  # 그 노드가 방문하지 않았다면,
                visited[i] = True
                queue.append(i) # 큐에 넣고 방문처리

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

bfs(visited, 1, graph)