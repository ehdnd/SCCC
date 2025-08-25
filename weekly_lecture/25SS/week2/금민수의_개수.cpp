#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void Solve() {
  int a, b;
  cin >> a >> b;

  int ans = 0;

  for (int k = 1; k < 10; ++k) {
    for (int m = 0; m < (1 << k); ++m) {
      string s;
      for (int i = k - 1; i >= 0; --i) {
        s.push_back((m >> i & 1) ? '7' : '4');
      }
      ll n = stoll(s);
      if (a <= n && n <= b) ans++;
    }
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}