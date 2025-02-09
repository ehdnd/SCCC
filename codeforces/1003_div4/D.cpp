#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

void Solve() {
  int N, M;
  cin >> N >> M;

  vector<pll> pfs;
  pfs.resize(N, {0, 0});

  for (int i = 0; i < N; ++i) {
    ll temp = 0;
    for (int j = 0; j < M; ++j) {
      ll val;
      auto& [sum, pf] = pfs[i];

      cin >> val;
      sum -= val;
      temp += val;
      pf -= temp;
    }
  }

  sort(all(pfs));

  ll ans = 0, prev_sum = 0;
  for (int i = 0; i < N; ++i) {
    auto& [sum, pf] = pfs[i];
    ans += prev_sum * M;
    ans -= pf;

    prev_sum -= sum;
  }

  cout << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}