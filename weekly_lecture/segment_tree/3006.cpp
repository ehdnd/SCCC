#include <bits/stdc++.h>
using namespace std;

int N, sz = 1;
vector<int> seg, idx;

void Solve() {
  cin >> N;
  while (sz < N) sz <<= 1;

  idx.resize(N + 1, 0);
  seg.resize(2 * sz, 0);

  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    idx[a] = i;
  }

  for (int i = 0; i < N; ++i) seg[sz + i] = 1;
  for (int i = sz - 1; i >= 1; --i) seg[i] = seg[i * 2] + seg[i * 2 + 1];

  for (int i = 1; i <= N / 2; ++i) {
    int a = sz + idx[i];
    int b = sz + idx[N + 1 - i] + 1;
    int c = sz + idx[i];
    int d = sz + idx[N + 1 - i];

    int sum_a = 0, l_a = sz;
    while (l_a < a) {
      if (l_a & 1) sum_a += seg[l_a++];
      if (a & 1) sum_a += seg[--a];
      l_a >>= 1, a >>= 1;
    }
    cout << sum_a << "\n";

    seg[c] = 0;
    while (c > 1) {
      c >>= 1;
      seg[c] = seg[c * 2] + seg[c * 2 + 1];
    }

    int sum_b = 0, r_b = sz + N;
    while (b < r_b) {
      if (b & 1) sum_b += seg[b++];
      if (r_b & 1) sum_b += seg[--r_b];
      b >>= 1, r_b >>= 1;
    }
    cout << sum_b << "\n";

    seg[d] = 0;
    while (d > 1) {
      d >>= 1;
      seg[d] = seg[d * 2] + seg[d * 2 + 1];
    }
  }

  if (N & 1) cout << 0 << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}