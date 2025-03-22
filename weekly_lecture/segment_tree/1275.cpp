#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, Q, sz = 1;
vector<ll> seg;

void Solve() {
  cin >> N >> Q;
  while (sz < N) sz <<= 1;
  seg.resize(sz * 2, 0);
  for (int i = 0; i < N; ++i) cin >> seg[sz + i];
  for (int i = sz - 1; i >= 1; --i) seg[i] = seg[i * 2] + seg[i * 2 + 1];

  while (Q--) {
    int x, y, a, b;
    cin >> x >> y >> a >> b;
    if (x > y) swap(x, y);
    x--, a--;

    ll res = 0;
    x += sz, y += sz;
    while (x < y) {
      if (x & 1) res += seg[x++];
      if (y & 1) res += seg[--y];
      x >>= 1, y >>= 1;
    }
    cout << res << "\n";

    a += sz;
    seg[a] = b;
    while (a > 1) {
      a >>= 1;
      seg[a] = seg[a * 2] + seg[a * 2 + 1];
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}