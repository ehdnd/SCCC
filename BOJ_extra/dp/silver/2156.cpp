#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int dp[10101], P[10101];
int N;

void Solve() {
  cin >> N;
  for (int i = 1; i <= N; i++) cin >> P[i];
  dp[1] = P[1];
  dp[2] = P[1] + P[2];
  for (int i = 3; i <= N; i++) {
    dp[i] = max({dp[i - 1], dp[i - 3] + P[i - 1] + P[i], dp[i - 2] + P[i]});
  }
  cout << dp[N];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}