#include <bits/stdc++.h>
using namespace std;

int N, S, M;
int V[51];
bool dp[51][1010];

// dp[i][j] i번째 곡을 j볼륨으로 연주 가능한가?
void Solve() {
  cin >> N >> S >> M;
  for (int i = 1; i <= N; i++) cin >> V[i];

  memset(dp, false, sizeof(dp));
  dp[0][S] = true;

  for (int i = 1; i <= N; i++) {
    bool flag = false;
    for (int j = 0; j <= M; j++) {
      if (dp[i - 1][j]) {
        if (j + V[i] <= M) {
          dp[i][j + V[i]] = true;
          flag = true;
        }
        if (j - V[i] >= 0) {
          dp[i][j - V[i]] = true;
          flag = true;
        }
      }
    }
    if (!flag) {
      cout << -1;
      return;
    }
  }

  for (int i = M; i >= 0; i--) {
    if (dp[N][i]) {
      cout << i;
      return;
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}