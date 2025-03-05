#include <bits/stdc++.h>
using namespace std;

int N, b_cnt, ans;
bool bis_m[20];
vector<vector<int>> board;

inline bool chk(int c) { return 0 <= c && c < N; }

void BT(int x) {
  if (x == 2 * N - 1) {
    ans = max(ans, b_cnt);
    return;
  }

  bool flag = false;

  for (int r = 0; r < N; ++r) {
    const int c = x - r;
    const int b_m = r - c + N - 1;

    if (chk(c) && board[r][c] && !bis_m[b_m]) {
      flag = true;

      bis_m[b_m] = 1;
      b_cnt++;

      BT(x + 1);

      bis_m[b_m] = 0;
      b_cnt--;
    }
  }

  if (!flag) BT(x + 1);
}

void Solve() {
  cin >> N;
  board.resize(N, vector<int>(N, 0));
  for (auto& r : board)
    for (auto& v : r) cin >> v;

  BT(0);

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}