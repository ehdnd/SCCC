#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int N;
int cnt, a, b, c;
int prev_dp[3], curr_dp[3];

void Solve() {
  cin >> a >> b >> c;
  prev_dp[0] = INF;
  prev_dp[1] = b;
  prev_dp[2] = c + prev_dp[1];

  for (int i = 1; i < N; i++) {
    cin >> a >> b >> c;
    curr_dp[0] = a + min({prev_dp[0], prev_dp[1]});
    curr_dp[1] = b + min({prev_dp[0], prev_dp[1], prev_dp[2], curr_dp[0]});
    curr_dp[2] = c + min({prev_dp[1], prev_dp[2], curr_dp[1]});

    swap(prev_dp, curr_dp);
  }

  cout << ++cnt << ". " << prev_dp[1] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  while (1) {
    cin >> N;
    if (!N) break;
    Solve();
  }
  return 0;
}