def in_range(x, y, n):
    return 1 <= x <= n and 1 <= y <= n

def main():
    n, t = map(int, input().split())
    r, c, d = input().split()
    r = int(r)
    c = int(c)
    
    # 방향을 나타내는 딕셔너리와 이동 벡터
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    # 초기 이동 방향
    dx, dy = directions[d]
    
    for _ in range(t):
        # 다음 위치 계산
        next_r = r + dx
        next_c = c + dy
        
        # 벽에 부딪히면 방향을 반대로 변경
        if not in_range(next_r, next_c, n):
            dx = -dx
            dy = -dy
            continue
            
        # 구슬 위치 업데이트
        r = next_r
        c = next_c
    
    print(r, c)

if __name__ == "__main__":
    main()