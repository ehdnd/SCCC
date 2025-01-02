#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAX = 101010;
const int INF = 1e9;
int N, cnt;
int G[MAX][3];
int dp[MAX][3];

void Solve() {
  for (int i = 0; i < N; i++)
    for (int j = 0; j < 3; j++) cin >> G[i][j];

  dp[0][0] = INF;  // 초기화좀 잘 해주자..
  dp[0][1] = G[0][1];
  dp[0][2] = G[0][2] + G[0][1];

  for (int i = 1; i < N; i++) {
    dp[i][0] = G[i][0] + min(dp[i - 1][0], dp[i - 1][1]);
    dp[i][1] =
        G[i][1] + min({dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]});
    dp[i][2] = G[i][2] + min({dp[i - 1][1], dp[i - 1][2], dp[i][1]});
  }

  cout << ++cnt << ". " << dp[N - 1][1] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  while (1) {
    cin >> N;
    if (!N) break;
    Solve();
  }
  return 0;
}