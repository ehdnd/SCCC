import sys

input = lambda: sys.stdin.readline().rstrip()


def isPossible(m, houses, C):
    cnt = 1
    # m 길이 기준으로 houses[0] 부터 거리 m 이상이면 cnt += 1
    p1, p2 = 0, 0
    while p2 < len(houses):
        if houses[p2] - houses[p1] >= m:
            cnt += 1
            p1 = p2
        p2 += 1

    # 설치 가능 공유기 개수가 C 이상이면 True 반환
    # -> m 보다 작은 거리는 모두 True
    # -> s = m + 1 로 s 를 이동하자
    if cnt >= C:
        return 1
    else:
        return 0


def jud(houses, C):
    s = 1
    e = houses[-1] - houses[0]
    while s <= e:
        m = (s + e) // 2
        if isPossible(m, houses, C):
            s = m + 1
        else:
            e = m - 1

    return e


N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])
print(jud(houses, C))
