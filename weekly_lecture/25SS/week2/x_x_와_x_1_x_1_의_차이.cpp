#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

void Solve() {
  ll x;
  cin >> x;

  vector<ll> ans;

  for (ll i = 1; i * i <= x + 1; ++i) {
    ll a = i;
    ll b = (x + 1) / i;

    if (a * b != x + 1) continue;

    ans.push_back(a);
    if (b <= x && a != b) ans.push_back(b);
  }

  sort(ans.begin(), ans.end());

  for (const ll& x : ans) cout << x << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}