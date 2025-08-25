#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9;

int N, K;
vector<vector<int>> dp;

void Solve() {
  cin >> N >> K;
  dp.resize(K + 1, vector<int>(N + 1, 0));

  for (auto& r : dp) r[0] = 1;
  for (int i = 1; i <= K; ++i)
    for (int j = 1; j <= N; ++j) dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;

  cout << dp[K][N];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}