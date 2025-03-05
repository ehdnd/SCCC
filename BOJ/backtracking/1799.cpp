#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, b_cnt[2], temp, ans;
vector<pii> bishops[2];
bool bis_p[20], bis_m[20];

void BT(int k, int b_idx, int sel) {
  if (b_idx == b_cnt[k]) {
    temp = max(temp, sel);
    return;
  }

  BT(k, b_idx + 1, sel);

  const auto& [r, c] = bishops[k][b_idx];
  int b_p = r + c, b_m = r - c + N - 1;

  if (bis_p[b_p] || bis_m[b_m]) return;

  bis_p[b_p] = 1, bis_m[b_m] = 1;
  BT(k, b_idx + 1, sel + 1);
  bis_p[b_p] = 0, bis_m[b_m] = 0;
}

void Solve() {
  cin >> N;
  int val;
  for (int r = 0; r < N; ++r)
    for (int c = 0; c < N; ++c) {
      cin >> val;
      if (val) bishops[(r + c) & 1].emplace_back(r, c);
    }

  for (int k = 0; k < 2; ++k) {
    temp = 0;
    b_cnt[k] = bishops[k].size();

    BT(k, 0, 0);

    ans += temp;
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}