#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pii = pair<int, int>;

// 항등원
const ll INF = 1e18;

int N, M;
vector<ll> seg, arr;

// 구간은 모두 [s,e)

ll Build(int node, int st, int ed) {
  // 리프 노드 조건
  if (ed - st == 1) return seg[node] = arr[st];

  int mid = st + (ed - st) / 2;
  return seg[node] =
             min(Build(node * 2, st, mid), Build(node * 2 + 1, mid, ed));
}

/// @brief
/// @param node 현재 노드의 고유 번호, 위치 (배열 인덱스)
/// @param st   현재 node가 책임지는 구간
/// @param ed   현재 node가 책임지는 구간
/// @param idx  업데이트할 위치
/// @param v    업데이트할 값
void Update(int node, int st, int ed, int idx, ll v) {
  if (idx < st || idx >= ed) return;
  // 리프 노드
  if (ed - st == 1) {
    seg[node] = v;
    return;
  }

  int mid = st + (ed - st) / 2;
  Update(node * 2, st, mid, idx, v);
  Update(node * 2 + 1, mid, ed, idx, v);
  seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
}

/// @brief
/// @param node
/// @param st
/// @param ed
/// @param l    값을 알고 싶어하는 구간 [l, r)
/// @param r    값을 알고 싶어하는 구간 [l, r)
/// @return
ll Query(int node, int st, int ed, int l, int r) {
  // 겹치지 않으면 항등원 반환
  if (r <= st || l >= ed) return INF;
  // 겹치면 값 반환
  if (l <= st && ed <= r) return seg[node];

  int mid = st + (ed - st) / 2;
  return min(Query(node * 2, st, mid, l, r),
             Query(node * 2 + 1, mid, ed, l, r));
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; ++i) {
    int a;
    cin >> a;
    arr.push_back(a);
  }

  // 충분한 크기임
  seg.assign(4 * N, INF);
  Build(1, 0, N);

  while (M--) {
    int a, b;
    cin >> a >> b;
    --a;
    cout << Query(1, 0, N, a, b) << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}