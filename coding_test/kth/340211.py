# https://school.programmers.co.kr/learn/courses/30/lessons/340211

def get_key(index, position):
    return f"{index}_{position[0]}_{position[1]}"


def solution(points, routes):
    robot_paths = {}

    for index, robot_routes in enumerate(routes):
        # 이동할 로봇 위치 및 포지션
        robot_num = robot_routes[0]
        robot_position = points[robot_num - 1]

        # 이동 경로 목표 지점
        target_robot_nums = robot_routes[1:]
        time = 0
        for target_robot_num in target_robot_nums:
            target_robot_position = points[target_robot_num - 1]
            move_r = target_robot_position[0] - robot_position[0]
            move_c = target_robot_position[1] - robot_position[1]

            robot_last_position = robot_position
            key = get_key(time, robot_last_position)
            time += 1
            if key in robot_paths:
                robot_paths[key] += 1
            else:
                robot_paths[key] = 1

            # move_r 부터 모두 이동
            move_r_direction = 1 if move_r > 0 else -1
            for _ in range(0, abs(move_r)):
                robot_last_position = [robot_last_position[0] + move_r_direction, robot_last_position[1]]
                key = get_key(time, robot_last_position)
                time += 1
                if key in robot_paths:
                    robot_paths[key] += 1
                else:
                    robot_paths[key] = 1

            move_c_direction = 1 if move_c > 0 else -1
            # move_c 부터 모두 이동
            for _ in range(0, abs(move_c)):
                robot_last_position = [robot_last_position[0], robot_last_position[1] + move_c_direction]
                key = get_key(time, robot_last_position)
                time += 1
                if key in robot_paths:
                    robot_paths[key] += 1
                else:
                    robot_paths[key] = 1

    return sum(1 for v in robot_paths.values() if v >= 2)


if __name__ == "__main__":
    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [2, 4]]
    # assert solution(points, routes) == 1
    # print(solution(points, routes))
    #
    print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))

    # print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]	))
