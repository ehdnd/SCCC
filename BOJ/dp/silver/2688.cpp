#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll dp[65][10];

// dp[i][j] i자리 j로 끝나는 개수
void MakeDP() {
  for (int i = 0; i <= 9; i++) dp[1][i] = 1;

  for (int i = 2; i <= 64; i++) {
    for (int j = 0; j <= 9; j++) {
      for (int k = 0; k <= j; k++) {
        dp[i][j] += dp[i - 1][k];
      }
    }
  }
}

void Solve() {
  int T;
  cin >> T;

  MakeDP();

  while (T--) {
    int N;
    ll res = 0;
    cin >> N;
    for (auto i : dp[N]) res += i;
    cout << res << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}