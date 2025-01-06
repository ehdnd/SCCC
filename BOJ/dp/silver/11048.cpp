#include <bits/stdc++.h>
using namespace std;

int N, M;
int candy[1010][1010];
int dp[1010][1010];

int dx[4] = {-1, -1, 0};
int dy[4] = {0, -1, -1};

inline bool chk(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++) cin >> candy[i][j];

  dp[0][0] = candy[0][0];

  for (int x = 0; x < N; x++) {
    for (int y = 0; y < M; y++) {
      for (int i = 0; i < 3; i++) {
        int px = x + dx[i];
        int py = y + dy[i];

        if (!chk(px, py)) continue;

        dp[x][y] = max(dp[x][y], dp[px][py] + candy[x][y]);
      }
    }
  }

  cout << dp[N - 1][M - 1];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}