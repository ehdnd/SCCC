#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int MAX = 1010101;
const int MOD = 1e9 + 9;
int N;
ll dp[MAX];

void MakeDP() {
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;

  for (int i = 4; i < MAX; i++)
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
}

void Solve() {
  cin >> N;
  cout << dp[N] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;

  MakeDP();

  while (T--) Solve();
  return 0;
}