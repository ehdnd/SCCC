#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using pii = pair<int, int>;

const int INF = 1e9;

int N, M, house_cnt, ans_dist = INF;
vector<pii> houses, chickens;
vector<int> houses_dist;

void BT(int idx, int selected_cnt) {
  if (selected_cnt == M || idx == chickens.size()) {
    if (selected_cnt > 0) {
      int total_dist = accumulate(all(houses_dist), 0);
      ans_dist = min(ans_dist, total_dist);
    }
    return;
  }

  BT(idx + 1, selected_cnt);

  vector<int> prev_dist = houses_dist;
  auto [cr, cc] = chickens[idx];

  for (int i = 0; i < house_cnt; ++i) {
    auto [hr, hc] = houses[i];
    houses_dist[i] = min(houses_dist[i], abs(hr - cr) + abs(hc - cc));
  }

  BT(idx + 1, selected_cnt + 1);

  swap(prev_dist, houses_dist);
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) {
      int x;
      cin >> x;
      if (x == 1) houses.emplace_back(i, j);
      if (x == 2) chickens.emplace_back(i, j);
    }

  house_cnt = (int)houses.size();
  houses_dist.resize(house_cnt, INF);

  BT(0, 0);

  cout << ans_dist;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}