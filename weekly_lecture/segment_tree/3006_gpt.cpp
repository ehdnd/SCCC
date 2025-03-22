#include <bits/stdc++.h>
using namespace std;

int N, sz = 1;
vector<int> seg, pos;

int Query(int l, int r) {
  int res = 0;
  l += sz, r += sz;
  while (l < r) {
    if (l & 1) res += seg[l++];
    if (r & 1) res += seg[--r];
    l /= 2, r /= 2;
  }
  return res;
}

void Update(int i, int val) {
  i += sz;
  seg[i] = val;
  for (i /= 2; i >= 1; i /= 2) seg[i] = seg[i * 2] + seg[i * 2 + 1];
}

void Solve() {
  cin >> N;
  while (sz < N) sz <<= 1;

  pos.resize(N + 1, 0);
  seg.resize(2 * sz, 0);

  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    pos[a] = i;
  }

  for (int i = 0; i < N; ++i) seg[sz + i] = 1;
  for (int i = sz - 1; i >= 1; --i) seg[i] = seg[i * 2] + seg[i * 2 + 1];

  for (int i = 1; i <= N / 2; ++i) {
    int res;

    res = Query(0, pos[i]);
    cout << res << "\n";
    Update(pos[i], 0);

    res = Query(pos[N + 1 - i] + 1, N);
    cout << res << "\n";
    Update(pos[N + 1 - i], 0);
  }

  if (N & 1) cout << 0 << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}