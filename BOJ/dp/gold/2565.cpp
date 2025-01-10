#include <bits/stdc++.h>
using namespace std;

const int MAX = 505;
int N, total;
int lines[MAX];
int dp[MAX];

void Solve() {
  cin >> N;
  total = N;
  while (N--) {
    int a, b;
    cin >> a >> b;
    lines[a] = b;
  }

  for (int i = 1; i < MAX; i++) {
    if (!lines[i]) continue;

    dp[i] = 1;
    for (int j = 1; j < i; j++) {
      if (!lines[j]) continue;

      if (lines[j] < lines[i]) dp[i] = max(dp[i], dp[j] + 1);
    }
  }

  cout << total - *max_element(dp, dp + MAX);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}