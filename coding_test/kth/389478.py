"""
@link https://school.programmers.co.kr/learn/courses/30/lessons/389478?language=python3
"""

def solution(n, w, num):
    row = (num - 1) // w
    col = (num - 1) % w

    # 홀수 층이면(오른쪽->왼쪽 배치) col 반전
    if row % 2 == 1:
        col = w - 1 - col

    # 전체 층 수
    total_rows = (n - 1) // w + 1
    remainder = n % w  # 마지막 층에 배치된 박스 개수 (0나오면 별도 처리)

    if remainder == 0:
        valid = total_rows
    else:
        last_row = total_rows - 1
        if last_row % 2 == 0:
            valid = total_rows if col < remainder else total_rows - 1
        else:
            valid = total_rows if col >= w - remainder else total_rows - 1

    return valid - row

if __name__ == '__main__':
    inp = [13, 3, 6, 4]
    # inp = [13, 3, 5, 3]
    # inp = [22, 6, 8, 3]

    assert solution(inp[0], inp[1], inp[2]) == inp[3]
