#include <bits/stdc++.h>
using namespace std;

const int MAX = 101010;
const int MOD = 9901;
int N;
int dp[MAX][3];

void MakeDP() {
  dp[1][0] = dp[1][1] = dp[1][2] = 1;
  for (int i = 2; i <= N; i++) {
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD;
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD;
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
  }
  return;
}

void Solve() {
  cin >> N;
  MakeDP();
  int res = dp[N][0] + dp[N][1] + dp[N][2];
  cout << res % MOD;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}