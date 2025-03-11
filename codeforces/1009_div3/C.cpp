#include <bits/stdc++.h>
using namespace std;

void Solve() {
  int x;
  cin >> x;

  if (((x - 1) & x) == 0) {
    cout << -1 << "\n";
    return;
  }

  if (((x + 1) & x) == 0) {
    cout << -1 << "\n";
    return;
  }

  int k = 32 - __builtin_clz(x);
  int y = (1 << (k - 1)) - 1;
  cout << y << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}