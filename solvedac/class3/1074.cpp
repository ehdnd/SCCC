#include <bits/stdc++.h>
using namespace std;

int N, R, C;

void jud(int r, int c, int n, int curr) {
  if (n == 0) {
    cout << curr;
    return;
  }

  int std = pow(2, n - 1);
  int plus = pow(2, (n - 1) * 2);

  if (r >= std) {
    curr += plus * 2;
    r -= std;
  }
  if (c >= std) {
    curr += plus;
    c -= std;
  }

  jud(r, c, --n, curr);
}

void Solve() {
  cin >> N >> R >> C;
  jud(R, C, N, 0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}