#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

const int MAX = 101010;
int N, cnt;
int G[MAX][3];
int dp[MAX];

void Solve() {
  for (int i = 0; i < N; i++)
    for (int j = 0; j < 3; j++) cin >> G[i][j];

  dp[0] = G[0][1];
  dp[1] = G[0][1] + G[1][1];

  for (int i = 2; i < N; i++) {
    dp[i] = G[i][1] +
            min({dp[i - 2] + G[i - 1][0], dp[i - 2] + G[i - 1][2], dp[i - 1]});
  }
  cout << ++cnt << ". " << dp[N - 1] << "\n";
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