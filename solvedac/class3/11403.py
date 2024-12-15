import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def floyd_warshall(G: list[list[int]], N: int):
    for x in range(0, N):
        for st in range(0, N):
            for ed in range(0, N):
                if G[st][x] and G[x][ed]:
                    G[st][ed] = 1
    return G


def solve() -> None:
    N = II()
    G = [list(MIS()) for _ in range(N)]
    G = floyd_warshall(G, N)
    for i in range(N):
        for j in range(N):
            print(G[i][j], end=" ")
        print()
    return


if __name__ == "__main__":
    solve()
