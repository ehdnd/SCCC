#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 101;
const int MAX_K = 10101;
const int INF = 1e9;
int N, K;
int cost[MAX_N];
int dp[MAX_N][MAX_K];

void Solve() {
  cin >> N >> K;
  for (int i = 1; i <= N; i++) cin >> cost[i];

  for (int i = 0; i <= N; i++)
    for (int j = 0; j <= K; j++) dp[i][j] = INF;

  dp[0][0] = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 0; j <= K; j++) {
      dp[i][j] = min(dp[i][j], dp[i - 1][j]);

      int jj = j + cost[i];
      if (jj <= K) dp[i][jj] = min(dp[i][jj], dp[i][j] + 1);
    }
  }

  cout << (dp[N][K] != INF ? dp[N][K] : -1);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}