# 너비우선탐색 (BFS, Breadth First Search)
# - 그래프를 탐색하는 알고리즘
# - 어떤 정점에서 시작해 다음 깊이의 정점으로 이동하기 전에 현재 깊이의 모든 정점을 탐색
# - 방문한 정점은 다시 방문하지 않음
# - 같은 가중치를 가진 그래프에서 최단거리 알고리즘으로 쓰임
# - 레이어별, 레벨별로 탐색

from collections import deque 

# 입력 받기
n, m = map(int, input().split()) # 미로 크기 n(행) m(열)
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

# 이동 방향 (상, 우, 하, 좌)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 방문 배열 초기화 (최단 거리 기록)
visited = [[0] * m for _ in range(n)]

# 초기 설정
queue = deque([(0, 0)]) # 초기 시작점
visited[0][0] = 1 # 시작 위치 방문 처리 (거리 1)

while queue:
    y, x = queue.popleft() # 현재 방문할 위치

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        # 범위를 벗어나거나 0 이거나 이미 방문한 경우
        if ny < 0 or ny >= n or nx <0 or nx >= m:
            continue
        if maze[ny][nx] == 0:
            continue
        if visited[ny][nx]:
            continue

        visited[ny][nx] = visited[y][x] + 1 # 최단 거리 갱신 
        queue.append((ny, nx))

# 최단 거리 출력
print(visited[n-1][m-1])
