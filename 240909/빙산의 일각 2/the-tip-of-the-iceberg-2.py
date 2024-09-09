# 입력 받기
N = int(input())
heights = [int(input()) for _ in range(N)]

def count_iceberg_chunks(sea_level):
    # 현재 해수면 높이보다 높은 빙산들만 확인
    is_in_air = [height > sea_level for height in heights]
    
    # 덩어리 개수 카운트
    chunk_count = 0
    in_chunk = False
    
    for i in range(N):
        if is_in_air[i]:
            if not in_chunk:
                chunk_count += 1
                in_chunk = True
        else:
            in_chunk = False
    
    return chunk_count

# 가능한 해수면 높이에서 최대 덩어리 개수 찾기
max_chunks = 0
for sea_level in range(1, max(heights) + 1):
    chunks = count_iceberg_chunks(sea_level)
    max_chunks = max(max_chunks, chunks)

# 결과 출력
print(max_chunks)