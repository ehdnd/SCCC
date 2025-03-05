#include <bits/stdc++.h>
using namespace std;

int N, ans;
int S[30][30];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) cin >> S[i][j];

  ans = 1e9;

  for (int m = 1; m < (1 << N); ++m) {
    if (m & 1) continue;

    int st = 0, li = 0;

    for (int i = 0; i < N; ++i)
      for (int j = i; j < N; ++j) {
        if (!(m & (1 << i)) && !(m & (1 << j)))
          st += S[i][j] + S[j][i];
        else if ((m & (1 << i)) && (m & (1 << j)))
          li += S[i][j] + S[j][i];
      }

    ans = min(ans, abs(st - li));
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}