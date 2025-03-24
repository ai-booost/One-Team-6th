from collections import Counter

def bfs(spots, route):
    idx = 0
    pa = []
    for i in range(len(route) - 1):
        sx, sy = spots[route[i] - 1]
        ex, ey = spots[route[i + 1] - 1]

        # x 좌표 맞추기
        while sx != ex:
            pa.append((sx, sy, idx))
            if sx < ex:
                sx += 1
            else:
                sx -= 1
            idx += 1

        # y 좌표 맞추기
        while sy != ey:
            pa.append((sx, sy, idx))
            if sy < ey:
                sy += 1
            else:
                sy -= 1
            idx += 1
    print(pa)
    pa.append((sx, sy, idx))
    print(pa)

    return pa

def solution(points, routes):
    spots = points
    second = []
    print(spots)

    for route in routes:
        print(route)
        second.extend(bfs(spots, route))

    res = 0
    print(second)
    temp = Counter(second)
    for i in temp.values():
        if i >= 2:
            res += 1

    return res

if __name__ == "__main__":
    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [2, 4]]
    # assert solution(points, routes) == 1
    # print(solution(points, routes))
    #
    print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))

    # print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]	))
