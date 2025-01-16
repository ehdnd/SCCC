#include <bits/stdc++.h>
using namespace std;

int N, cnt;
bool vis[15], diag1[30], diag2[30];

void BT(int row) {
  if (row == N) {
    cnt++;
    return;
  }

  for (int col = 0; col < N; col++) {
    int d1 = row + col;
    int d2 = row - col + N - 1;
    if (vis[col] || diag1[d1] || diag2[d2]) continue;

    vis[col] = 1;
    diag1[d1] = 1;
    diag2[d2] = 1;
    BT(row + 1);
    vis[col] = 0;
    diag1[d1] = 0;
    diag2[d2] = 0;
  }
}

void Solve() {
  cin >> N;
  BT(0);
  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}