#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int dp[11][222][222];

void Solve() {
  cin >> N >> M >> K;

  for (int p = 1; p <= M; ++p) {
    dp[0][0][p] = 1;
  }

  for (int j = 1; j <= M; ++j) {
    for (int p = 1; p <= M; ++p) {
      dp[1][j][p] = (p <= j) ? 1 : 0;
    }
  }

  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= M; ++j) {
      for (int p = j - 1; p >= 1; --p) {
        dp[i][j][p] = dp[i][j][p + 1] + dp[i - 1][j - p][p];
      }
    }
  }

  int p = 1;
  vector<int> ans;

  while (N) {
    for (int x = p; x <= M; ++x) {
      int cnt = dp[N - 1][M - x][x];

      if (cnt >= K) {
        ans.push_back(x);
        p = x;
        N--;
        M -= x;
        break;
      } else {
        K -= cnt;
      }
    }
  }

  for (int& a : ans) cout << a << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}