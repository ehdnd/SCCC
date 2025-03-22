#include <bits/stdc++.h>
using namespace std;

int N, M, sz, idx;
vector<int> seg, arr;

void Solve() {
  cin >> N >> M;
  sz = 1;
  idx = M - 1;
  while (sz < N + M) sz *= 2;
  seg.assign(sz * 2, 0);
  arr.assign(N, 0);

  for (int i = 0; i < N; ++i) arr[i] = i + M;

  for (int i = 0; i < N; ++i) seg[sz + arr[i]] = 1;
  for (int i = sz - 1; i >= 1; --i) seg[i] = seg[i * 2] + seg[i * 2 + 1];

  while (M--) {
    int a = sz, q;
    cin >> q;
    q--;

    int qi = sz + arr[q];

    int c = qi, res = 0;
    while (a < c) {
      if (a & 1) res += seg[a++];
      if (c & 1) res += seg[--c];
      a /= 2, c /= 2;
    }
    cout << res << " ";

    seg[qi] = 0;
    for (qi /= 2; qi >= 1; qi /= 2) seg[qi] = seg[qi * 2] + seg[qi * 2 + 1];

    arr[q] = idx--;

    qi = sz + arr[q];
    seg[qi] = 1;
    for (qi /= 2; qi >= 1; qi /= 2) seg[qi] = seg[qi * 2] + seg[qi * 2 + 1];
  }

  cout << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}