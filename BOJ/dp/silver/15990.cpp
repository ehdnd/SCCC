#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 1e9 + 9;
ll dp[101010][3];
int N;

void MakeDP() {
  dp[1][0] = 1;
  dp[2][1] = 1;
  dp[3][0] = dp[3][1] = dp[3][2] = 1;

  for (int i = 4; i < 101010; i++) {
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD;
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % MOD;
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD;
  }
}

void Solve() {
  cin >> N;
  ll res = (dp[N][0] + dp[N][1] + dp[N][2]) % MOD;
  cout << res << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  MakeDP();
  while (T--) Solve();
  return 0;
}