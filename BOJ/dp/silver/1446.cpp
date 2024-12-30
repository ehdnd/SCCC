#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int INF = 101010;
int N, D;
int dp[10101];
vector<pii> lines[10101];

void Solve() {
  cin >> N >> D;

  for (int i = 0; i < N; i++) {
    int st, ed, w;
    cin >> st >> ed >> w;
    if (ed > D) continue;
    lines[ed].emplace_back(st, w);
  }

  fill(dp + 1, dp + D + 1, INF);

  for (int i = 1; i <= D; i++) {
    dp[i] = dp[i - 1] + 1;
    for (auto [st, w] : lines[i]) {
      dp[i] = min(dp[i], dp[st] + w);
    }
  }

  cout << dp[D];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}