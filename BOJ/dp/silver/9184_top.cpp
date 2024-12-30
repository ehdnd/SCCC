#include <bits/stdc++.h>
using namespace std;

int dp[21][21][21];

int WRecursion(int a, int b, int c) {
  if (a <= 0 || b <= 0 || c <= 0) return 1;
  if (a > 20 || b > 20 || c > 20) return WRecursion(20, 20, 20);

  if (dp[a][b][c] != -1) return dp[a][b][c];

  if (a < b && b < c)
    return dp[a][b][c] = WRecursion(a, b, c - 1) + WRecursion(a, b - 1, c - 1) -
                         WRecursion(a, b - 1, c);

  return dp[a][b][c] = WRecursion(a - 1, b, c) + WRecursion(a - 1, b - 1, c) +
                       WRecursion(a - 1, b, c - 1) -
                       WRecursion(a - 1, b - 1, c - 1);
}

void Solve() {
  memset(dp, -1, sizeof(dp));
  while (1) {
    int a, b, c, res;
    cin >> a >> b >> c;
    if (a == -1 && b == -1 && c == -1) return;
    res = WRecursion(a, b, c);
    cout << "w(" << a << ", " << b << ", " << c << ") = " << res << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}