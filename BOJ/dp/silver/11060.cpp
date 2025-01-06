#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int N;
int maze[1010];
int dp[1010];

void Solve() {
  cin >> N;

  fill(dp, dp + 1010, INF);
  dp[0] = 0;

  for (int i = 0; i < N; i++) {
    cin >> maze[i];
    for (int j = 0; j < i; j++) {
      if (j + maze[j] >= i && dp[j] != INF) {
        dp[i] = min(dp[i], dp[j] + 1);
      }
    }
  }

  cout << (dp[N - 1] != INF ? dp[N - 1] : -1);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}