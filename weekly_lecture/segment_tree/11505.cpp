#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9 + 7;

int N, M, K, sz;

vector<ll> seg;

void Update(int i, int val) {
  int idx = sz + i;
  seg[idx] = val;

  while (idx > 1) {
    idx /= 2;
    seg[idx] = (seg[idx * 2] * seg[idx * 2 + 1]) % MOD;
  }
}

int Query(int l, int r) {
  ll res = 1;
  l += sz, r += sz;

  while (l < r) {
    if (l & 1) {
      res *= seg[l];
      res %= MOD;
      l++;
    }

    if (r & 1) {
      r--;
      res *= seg[r];
      res %= MOD;
    }

    l /= 2;
    r /= 2;
  }

  return res;
}

void Solve() {
  cin >> N >> M >> K;

  sz = 1;
  while (sz < N) sz *= 2;

  seg.resize(2 * sz, 1);
  for (int i = 0; i < N; ++i) cin >> seg[sz + i];

  for (int i = sz - 1; i >= 1; --i)
    seg[i] = (seg[i * 2] * seg[i * 2 + 1]) % MOD;

  int Q = M + K;
  while (Q--) {
    int a, b, c;
    cin >> a >> b >> c;
    b--;

    if (a == 1) Update(b, c);
    if (a == 2) cout << Query(b, c) << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}