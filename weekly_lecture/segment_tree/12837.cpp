#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, Q, sz = 1;
vector<ll> seg;

void Solve() {
  cin >> N >> Q;
  while (sz < N) sz <<= 1;
  seg.resize(sz * 2, 0);

  while (Q--) {
    int a, b, c;
    cin >> a >> b >> c;
    b--;
    if (a == 1) {
      b += sz;
      seg[b] += c;

      while (b > 1) {
        b >>= 1;
        seg[b] = seg[b * 2] + seg[b * 2 + 1];
      }
    }
    if (a == 2) {
      ll ans = 0;
      b += sz, c += sz;
      while (b < c) {
        if (b & 1) ans += seg[b++];
        if (c & 1) ans += seg[--c];
        b >>= 1, c >>= 1;
      }
      cout << ans << "\n";
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}