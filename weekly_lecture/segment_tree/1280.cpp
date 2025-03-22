#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9 + 7;
const int BASE = 1 << 18;

int N;
vector<ll> sum, cnt;
ll ans = 1;

ll Calculate(vector<ll>& seg, int l, int r) {
  ll ret = 0;
  l += BASE, r += BASE;
  while (l < r) {
    if (l & 1) ret = ret + seg[l++];
    if (r & 1) ret = ret + seg[--r];
    l /= 2, r /= 2;
  }
  return ret;
}

void Update(vector<ll>& seg, int i, int val) {
  i += BASE;
  seg[i] += val;
  for (i /= 2; i >= 1; i /= 2) seg[i] = seg[i * 2] + seg[i * 2 + 1];
}

void Solve() {
  cin >> N;

  sum.resize(BASE * 2, 0);
  cnt.resize(BASE * 2, 0);

  for (int i = 0; i < N; ++i) {
    ll x;
    cin >> x;

    ll temp = 0;
    temp += Calculate(cnt, 0, x) * x - Calculate(sum, 0, x);
    temp += Calculate(sum, x + 1, BASE) - Calculate(cnt, x + 1, BASE) * x;
    temp %= MOD;

    if (i) ans = (ans * temp) % MOD;

    Update(cnt, x, 1);
    Update(sum, x, x);
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}