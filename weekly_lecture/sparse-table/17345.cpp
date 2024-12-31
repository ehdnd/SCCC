#include <bits/stdc++.h>
using namespace std;

const int MAX = 505050;
const int MAX_D = 19;  // 2^k >= MAX인 최소의 k
int M, Q;
int sparse_table[MAX][MAX_D];

void Solve() {
  cin >> M;
  // sparse_table[i][j] = 정점 i에서 2^j번 이동한 후의 정점
  for (int i = 1; i <= M; i++) cin >> sparse_table[i][0];

  // 작은 j부터 배열을 채워가면서 전체 배열을 채울 수 있다.
  for (int j = 1; j < MAX_D; j++)
    for (int i = 1; i <= M; i++)
      sparse_table[i][j] = sparse_table[sparse_table[i][j - 1]][j - 1];

  cin >> Q;
  while (Q--) {
    int n, x;
    cin >> n >> x;

    // 제일 큰 비트부터, n이 2^j 이상이면 사용해서 점프
    for (int j = MAX_D - 1; j >= 0; --j)
      if (n >= 1 << j) {
        n -= (1 << j);
        // x에서 2^j 번 이동해서 건너뜀
        x = sparse_table[x][j];
      }
    cout << x << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}