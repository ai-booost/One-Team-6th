# # 너비우선탐색 (DFS, Depth First Search)
# # - 그래프를 탐색하는 알고리즘
# # - 어떤 노드부터 시작해 인접한 노드들을 재귀적으로 방문
# # - 방문한 정점은 다시 방문하지 않음
# # - 각 분기마다 가장 멀리 있는 노드까지 탐색

# 입력
n = int(input().strip())  # n x n 지역 크기
area = [list(map(int, input().split())) for _ in range(n)]  # 높이 정보

# 이동 방향 (상, 우, 하, 좌)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 최대 안전 영역 개수 초기화
max_cnt = 0

def dfs(y, x, h):
    stack = [(y, x)]
    visited[y][x] = True

    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and area[ny][nx] > h:
                visited[ny][nx] = True
                stack.append((ny, nx))  # 스택에 추가하여 반복 탐색

for h in range(0, 101):  # 가능한 모든 강수량 높이(h)에 대해 반복
    visited = [[False] * n for _ in range(n)]  # 방문 여부 배열 초기화
    cnt = 0  # 현재 높이(h)에서의 안전 영역 개수

    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:  # 물에 잠기지 않고 방문하지 않은 곳
                dfs(i, j, h)  # 스택 기반 DFS 사용
                cnt += 1

    max_cnt = max(max_cnt, cnt)  # 최대 안전 영역 갱신

# 최대 안전 영역 개수 출력
print(max_cnt)



# # 재귀 -> 런타임 에러
# import sys

# sys.setrecursionlimit(10000) # 런타임 에러 방지

# # 입력
# n = int(input().strip()) # n x n 지역 크기 
# area = [list(map(int, input().split())) for _ in range(n)] # 높이 정보

# # 이동 방향 (상, 우, 하, 좌)
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# # 최대 안전 영역 개수 초기화
# max_cnt = 0

# def dfs(y, x, h):
#     visited[y][x] = True

#     for i in range(4):
#         ny, nx = y + dy[i], x + dx[i]
#         if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and area[ny][nx] > h:
#             dfs(ny, nx, h)

# for h in range(0, 101): # 가능한 모든 강수량 높이(h)에 대해 반복
    
#     visited = [[False] * n for _ in range(n)] # 방문 여부 배열 초기화

#     cnt = 0 # 현재 높이(h)에서의 안전 영역 개수

#     for i in range(n):
#         for j in range(n):
#             if area[i][j] > h and not visited[i][j]: # 물에 잠기지 않고 방문하지 않은 곳
#                 dfs(i, j, h)
#                 cnt += 1

#     max_cnt = max(max_cnt, cnt) # 최대 안전 영역 갱신

# # 최대 안전 영역 개수 출력
# print(max_cnt)


# # BFS 풀이

# from collections import deque

# n = int(input().strip())
# area = [list(map(int, input().split())) for _ in range(n)]

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# max_cnt = 0

# def bfs(y, x, h):
#     queue = deque([(y, x)])
#     visited[y][x] = True

#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and area[ny][nx] > h:
#                 visited[ny][nx] = True
#                 queue.append((ny, nx))

# for h in range(0, 101):
#     visited = [[False] * n for _ in range(n)]
#     cnt = 0

#     for i in range(n):
#         for j in range(n):
#             if area[i][j] > h and not visited[i][j]:
#                 bfs(i, j, h)  
#                 cnt += 1

#     max_cnt = max(max_cnt, cnt)

# print(max_cnt)