#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N;
int P[10101];
int dp[10101];

void Solve() {
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> P[i];
    dp[i] = P[i];
  }

  for (int i = 2; i <= N; i++) {
    for (int j = 1; j < i; j++) {
      dp[i] = min(dp[i], dp[j] + P[i - j]);
    }
  }

  cout << dp[N];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}