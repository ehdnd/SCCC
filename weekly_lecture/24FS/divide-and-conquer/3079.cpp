#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, M;
vector<ll> T;

bool isPoss(ll val) {
  ll p = 0;
  for (ll& t : T) {
    p += (val / t);
    if (M <= p) return true;
  }
  return false;
}

void Solve() {
  cin >> N >> M;
  T.resize(N, 0);
  for (ll& t : T) cin >> t;

  ll lo = 1, hi = 1e18;
  while (lo <= hi) {
    ll mid = lo + (hi - lo) / 2;

    if (isPoss(mid))
      hi = mid - 1;
    else
      lo = mid + 1;
  }

  cout << lo;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}