#include <bits/stdc++.h>
using namespace std;

int N;
int box[1010];
int dp[1010];

void Solve() {
  cin >> N;

  fill(dp, dp + N, 1);

  for (int i = 0; i < N; i++) {
    cin >> box[i];

    for (int j = 0; j < i; j++) {
      if (box[j] < box[i]) dp[i] = max(dp[i], dp[j] + 1);
    }
  }

  cout << *max_element(dp, dp + N);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}