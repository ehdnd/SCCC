#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 1'000'000'000;
ll N, res;
ll dp[101][10];

// dp[i][j] 길이가 i인 j로 끝나는 계단수의 개수
void MakeDP() {
  for (int j = 1; j < 10; j++) dp[1][j] = 1;
  for (int i = 2; i <= N; i++) {
    dp[i][0] = dp[i - 1][1];
    for (int j = 1; j <= 8; j++)
      dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;
    dp[i][9] = dp[i - 1][8];
  }
}

void Solve() {
  cin >> N;
  MakeDP();
  for (int j = 0; j < 10; j++) res += dp[N][j];
  cout << res % MOD;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}