import itertools

# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

homes = [] # 집 위치
chickens = [] # 치킨집 위치

# 집 or 치킨집 위치 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

# 모든 치킨집 중에서 m개 선택
chicken_combinations = list(itertools.combinations(chickens, m))

# 최소 치킨 거리
min_distance = float('inf')

for combi in chicken_combinations:
    total_distance = 0 # 모든 집의 치킨 거리 합산
    for hx, hy in homes:
        distance = float('inf')
        for cx, cy in combi:
            distance = min(distance, abs(hx - cx) + abs(hy - cy)) # 각 집마다 가장 가까운 치킨 거리
        total_distance += distance
    
    min_distance = min(min_distance, total_distance)

# 최소 치킨 거리 출력
print(min_distance)