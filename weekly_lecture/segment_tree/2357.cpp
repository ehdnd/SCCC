#include <bits/stdc++.h>
using namespace std;

const int INF = 2e9;

int N, M, sz;
vector<int> max_s, min_s;

int FindMax(int l, int r) {
  int res = 0;
  l += sz, r += sz;

  while (l < r) {
    if (l & 1) res = max(res, max_s[l++]);
    if (r & 1) res = max(res, max_s[--r]);
    l /= 2, r /= 2;
  }
  return res;
}

int FindMin(int l, int r) {
  int res = INF;
  l += sz, r += sz;

  while (l < r) {
    if (l & 1) res = min(res, min_s[l++]);
    if (r & 1) res = min(res, min_s[--r]);

    l /= 2, r /= 2;
  }
  return res;
}

void Solve() {
  cin >> N >> M;

  sz = 1;
  while (sz < N) sz *= 2;

  max_s.resize(2 * sz, 0);
  min_s.resize(2 * sz, INF);

  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    max_s[sz + i] = min_s[sz + i] = a;
  }

  for (int i = sz - 1; i >= 1; --i) {
    max_s[i] = max(max_s[i * 2], max_s[i * 2 + 1]);
    min_s[i] = min(min_s[i * 2], min_s[i * 2 + 1]);
  }

  while (M--) {
    int l, r;
    cin >> l >> r;
    l--;

    cout << FindMin(l, r) << " " << FindMax(l, r) << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}