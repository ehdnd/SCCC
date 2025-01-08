#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, K;
vector<int> P;
vector<ll> dp;

void Solve() {
  cin >> N >> K;

  P.resize(N);
  for (auto& p : P) cin >> p;

  dp.resize(K + 1);
  dp[0] = 1;

  for (const auto& p : P)
    for (int j = p; j <= K; j++) dp[j] += dp[j - p];

  cout << dp[K];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}