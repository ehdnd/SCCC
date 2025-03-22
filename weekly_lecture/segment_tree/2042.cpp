#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, M, K, sz;
vector<ll> seg;

void Construct() {
  for (int i = sz - 1; i >= 1; --i) {
    seg[i] = seg[2 * i] + seg[2 * i + 1];
  }
}

void Update(int i, ll val) {
  int idx = sz + i;
  seg[idx] = val;

  while (idx > 1) {
    idx /= 2;
    seg[idx] = seg[2 * idx] + seg[2 * idx + 1];
  }
}

ll sum(int l, int r, int node_num, int node_l, int node_r) {
  // 현재 노드 구간과 목표 구간 [l, r) 겹치지 않으면 항등원 (0) 리턴
  if (r <= node_l || node_r <= l) return 0;

  // 현재 노드의 구간이 목표 구간에 완전히 포함
  if (l <= node_l && node_r <= r) return seg[node_num];

  int mid = (node_l + node_r) / 2;
  return sum(l, r, node_num * 2, node_l, mid) +
         sum(l, r, node_num * 2 + 1, mid, node_r);
}

ll query(int l, int r) {
  ll result = 0;
  l += sz, r += sz;  // 리프 노드 인덱스로 변환

  while (l < r) {
    // l이 홀수: seg[l]이 구간에 포함
    if (l & 1) {
      result += seg[l];
      l++;
    }

    // r이 홀수: seg[r-1]이 구간에 포함
    if (r & 1) {
      r--;
      result += seg[r];
    }

    // 다음 레벨로 올라감
    l /= 2;
    r /= 2;
  }

  return result;
}

void Solve() {
  cin >> N >> M >> K;

  // sz: N 이상인 최소의 2의 거듭제곱 (2^k 꼴)
  // sz: 포화 이진 트리로 만들기 위한 '리프 노드'의 개수
  sz = 1;
  while (sz < N) sz *= 2;

  // 전체 세그먼트 트리 배열의 크기는 2 * sz
  // 리프 노드는 인덱스 [sz, 2*sz)
  seg.resize(2 * sz, 0);

  // 리프 노드 채우기: 인덱스 [sz, sz + N)
  for (int i = 0; i < N; ++i) cin >> seg[sz + i];

  // 남은 리프 노드는 항등원(0) 으로 채우기
  for (int i = N; i < sz; ++i) seg[sz + i] = 0;

  Construct();

  int Q = M + K;
  while (Q--) {
    int a, b;
    ll c;
    cin >> a >> b >> c;
    b--;

    if (a == 1) {
      Update(b, c);
    }
    if (a == 2) {
      // [b, c) 내부적으로 처리
      cout << sum(b, c, 1, 0, sz) << "\n";
      // cout << query(b, c) << "\n";
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}