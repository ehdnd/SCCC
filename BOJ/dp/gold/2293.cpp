#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> P;
int prev_dp[10101];
int curr_dp[10101];

void Solve() {
  cin >> N >> K;
  P.resize(N);
  for (auto& p : P) cin >> p;

  // coin(n,k) 가 1~n번째 동전만 사용해서 k원을 나타내는 가짓수라고 하자.
  curr_dp[0] = prev_dp[0] = 1;

  for (const auto& p : P) {
    for (int k = 1; k <= K; k++) {
      if (p > k) {
        curr_dp[k] = prev_dp[k];
      } else {
        curr_dp[k] = curr_dp[k - p] + prev_dp[k];
      }
    }

    swap(curr_dp, prev_dp);
  }

  cout << prev_dp[K];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}