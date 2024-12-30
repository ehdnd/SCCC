#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N;
int board[101][101];
ll dp[101][101];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++) cin >> board[i][j];

  dp[0][0] = 1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      int jump = board[i][j];
      if (dp[i][j] == 0 || jump == 0) continue;
      if (i + jump < N) dp[i + jump][j] += dp[i][j];
      if (j + jump < N) dp[i][j + jump] += dp[i][j];
    }
  }
  cout << dp[N - 1][N - 1];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}