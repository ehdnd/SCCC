#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N;
vector<vector<int>> dp;
vector<vector<pii>> decision;
string st, ed;

void Solve() {
  cin >> N >> st >> ed;

  // i ~ N번째 나사가 j만큼 누적 회전했을 때 최소 횟수
  dp.resize(N + 1, vector<int>(10, 0));
  decision.resize(N + 1, vector<pii>(10, {0, 0}));

  for (int pos = N - 1; pos >= 0; --pos) {
    for (int offset = 0; offset < 10; ++offset) {
      int a = st[pos] - '0';
      int target = ed[pos] - '0';

      int curr = (a + offset) % 10;
      int diff = (10 + target - curr) % 10;  // 왼쪽

      int c_l = diff + dp[pos + 1][(offset + diff) % 10];  // 누적 회전량 전달
      int c_r = (10 - diff) + dp[pos + 1][offset];

      if (c_l < c_r) {
        dp[pos][offset] = c_l;
        decision[pos][offset] = {diff, (offset + diff) % 10};
      } else {
        dp[pos][offset] = c_r;
        decision[pos][offset] = {diff - 10, offset};
      }
    }
  }

  cout << dp[0][0] << "\n";

  int cum = 0;
  for (int pos = 0; pos < N; ++pos) {
    int mv = decision[pos][cum].first;
    cout << pos + 1 << " " << mv << "\n";

    cum = decision[pos][cum].second;
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}