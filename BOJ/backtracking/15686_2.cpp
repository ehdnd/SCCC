#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, M, ans_dist;
int board[50][50];
vector<pii> houses, chickens, selected;

void BT(int chicken_idx, int chicken_cnt, int curr_dist) {
  if (chicken_idx >= chickens.size()) {
    if (0 < chicken_cnt && chicken_cnt <= M) {
      ans_dist = min(ans_dist, curr_dist);
    }
    return;
  };

  BT(chicken_idx + 1, chicken_cnt, curr_dist);

  int each_dist;
  curr_dist = 0;
  selected.push_back(chickens[chicken_idx]);

  for (const auto& [hr, hc] : houses) {
    each_dist = 1e9;

    for (const auto& [cr, cc] : selected) {
      each_dist = min(each_dist, abs(hr - cr) + abs(hc - cc));
    }
    curr_dist += each_dist;
  }

  BT(chicken_idx + 1, chicken_cnt + 1, curr_dist);

  selected.pop_back();
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> board[i][j];

      if (board[i][j] == 1)
        houses.emplace_back(i, j);
      else if (board[i][j] == 2)
        chickens.emplace_back(i, j);
    }
  }

  ans_dist = 1e9;

  BT(0, 0, 0);

  cout << ans_dist;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}