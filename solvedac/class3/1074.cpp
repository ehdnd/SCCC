#include <bits/stdc++.h>
using namespace std;

int N, R, C, cnt;

void BT(int r, int c, int n) {
  if (n == 0) {
    if (r == R && c == C) cout << cnt;
    cnt++;
    return;
  }

  n--;
  int dd = pow(2, n);
  BT(r, c, n);
  BT(r, c + dd, n);
  BT(r + dd, c, n);
  BT(r + dd, c + dd, n);
}

void Solve() {
  cin >> N >> R >> C;

  BT(0, 0, N);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}