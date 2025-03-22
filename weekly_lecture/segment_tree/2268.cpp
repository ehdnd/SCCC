#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, M, sz = 1;
vector<ll> seg;

void Solve() {
  cin >> N >> M;
  while (sz < N) sz *= 2;
  seg.resize(sz * 2, 0);

  while (M--) {
    int a, b, c;
    cin >> a >> b >> c;
    if (a == 0) {
      if (b > c) swap(b, c);
      b--;
      ll res = 0;
      b += sz, c += sz;
      while (b < c) {
        if (b & 1) res += seg[b++];
        if (c & 1) res += seg[--c];
        b /= 2, c /= 2;
      }
      cout << res << "\n";
    } else {
      b--;
      b += sz;
      seg[b] = c;
      for (b /= 2; b >= 1; b /= 2) seg[b] = seg[b * 2] + seg[b * 2 + 1];
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}