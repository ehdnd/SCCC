#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

const ll INF = 1e18;
const pll IDENTITY = {INF, -1};

int N, M;
vector<ll> arr;
vector<pll> seg;

pll Build(int node, int st, int ed) {
  if (ed - st == 1) return seg[node] = {arr[st], st};
  int mid = (st + ed) / 2;
  return seg[node] =
             min(Build(node * 2, st, mid), Build(node * 2 + 1, mid, ed));
}

void Update(int node, int st, int ed, int idx, ll v) {
  if (idx < st || ed <= idx) return;
  if (ed - st == 1) {
    seg[node] = {v, idx};
    return;
  }
  int mid = (st + ed) / 2;
  Update(node * 2, st, mid, idx, v);
  Update(node * 2 + 1, mid, ed, idx, v);
  seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
}

pll Query(int node, int st, int ed, int l, int r) {
  if (r <= st || l >= ed) return IDENTITY;
  if (l <= st && ed <= r) return seg[node];
  int mid = st + (ed - st) / 2;
  return min(Query(node * 2, st, mid, l, r),
             Query(node * 2 + 1, mid, ed, l, r));
}

void Solve() {
  cin >> N;
  seg.assign(4 * N, IDENTITY);

  arr.resize(N);
  for (auto& x : arr) cin >> x;

  Build(1, 0, N);

  cin >> M;
  for (int i = 0; i < M; ++i) {
    ll a, b, c;
    cin >> a >> b >> c;
    if (a == 1)
      Update(1, 0, N, b - 1, c);
    else
      cout << Query(1, 0, N, b - 1, c).second + 1 << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}