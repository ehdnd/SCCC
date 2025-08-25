#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pii = pair<int, int>;

void Solve() {
  int N;
  cin >> N;

  if (N == 1) {
    int a;
    cin >> a;
    cout << a << "\n";
    return;
  }

  int ans = 0;

  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    ans += a;
  }

  ans = ans - N + 1;
  cout << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}