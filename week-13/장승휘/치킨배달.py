from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# 모든 치킨집 중 m개의 치킨집을 뽑는 조합
candidates = list(combinations(chicken, m))

# 치킨 거리의 합 계산
def get_sum(candidate):
    result = 0
    for hx, hy in house: # 모든 집에 대해 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp # 가장 가까운 치킨집까지의 거리를 result에 더해줌
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합이 최소일 때 찾기
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)