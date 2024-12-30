#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int dp[21][21][21];

void MakeDP() {
  for (int a = 0; a <= 20; a++)
    for (int b = 0; b <= 20; b++) {
      for (int c = 0; c <= 20; c++) {
        if (a == 0 || b == 0 || c == 0)
          dp[a][b][c] = 1;
        else if (a < b && b < c)
          dp[a][b][c] = dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c];
        else
          dp[a][b][c] = dp[a - 1][b][c] + dp[a - 1][b - 1][c] +
                        dp[a - 1][b][c - 1] - dp[a - 1][b - 1][c - 1];
      }
    }
}

int GetDP(int a, int b, int c) {
  if (a <= 0 || b <= 0 || c <= 0) return 1;
  if (a > 20 || b > 20 || c > 20) return dp[20][20][20];
  return dp[a][b][c];
}

void Solve() {
  MakeDP();
  while (1) {
    int a, b, c, res;
    cin >> a >> b >> c;
    if (a == -1 && b == -1 && c == -1) return;
    res = GetDP(a, b, c);
    cout << "w(" << a << ", " << b << ", " << c << ") = " << res << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}