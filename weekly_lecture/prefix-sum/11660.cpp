#include <bits/stdc++.h>
using namespace std;

int N, M;
int prefix_sum[1025][1025];

void MakePrefixSum() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      int a;
      cin >> a;
      prefix_sum[i + 1][j + 1] =
          prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + a;
    }
  }
}

void Solve() {
  cin >> N >> M;
  MakePrefixSum();
  for (int i = 0; i < M; i++) {
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    cout << prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] -
                prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]
         << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}