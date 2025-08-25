#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

const ll INF = 1e9 + 1;

ll N;
vector<pll> A;

void Solve() {
  cin >> N;
  for (int i = 0; i < N; ++i) {
    ll a, b;
    cin >> a >> b;
    A.emplace_back(a, b);
  }
  sort(all(A));

  ll res = 0, l = -INF, r = -INF;
  for (auto [a, b] : A) {
    if (r < a) {
      res += r - l;
      l = a;
      r = b;
    } else {
      r = max(r, b);
    }
  }
  res += r - l;
  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}