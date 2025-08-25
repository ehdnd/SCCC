import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N = II()
        # 2 * N 질의 시작
        dic = defaultdict(list)

        for i in range(1, N + 1):
            all_nodes = " ".join(map(str, range(1, N + 1)))
            query = f"? {i} {N} {all_nodes}"

            print(query)
            sys.stdout.flush()

            dic[II()].append(i)

        max_len = max(dic.keys())
        st_node = dic[max_len][0]

        path = [st_node]

        while len(path) < max_len:
            cur_path_len = len(path)
            len_needed = max_len - cur_path_len

            candidates = dic[len_needed]

            while len(candidates) > 1:
                mid = len(candidates) // 2
                half = candidates[:mid]
                q = path + half
                print(f"? {st_node} {len(q)} {' '.join(map(str, q))}")
                sys.stdout.flush()

                res = II()

                if res > cur_path_len:
                    candidates = half
                else:
                    candidates = candidates[mid:]

            next_node = candidates[0]
            path.append(next_node)

        ans = " ".join(map(str, path))
        print(f"! {max_len} {ans}")
        sys.stdout.flush()

    return


if __name__ == "__main__":
    solve()
