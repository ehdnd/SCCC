#include <bits/stdc++.h>
using namespace std;

void Solve() {
  int l, r, d, u;
  cin >> l >> r >> d >> u;
  if (l == r && r == d && d == u)
    cout << "Yes\n";
  else
    cout << "No\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}