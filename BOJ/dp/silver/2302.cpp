#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N;
int M;
ll dp[41];
bool vip[41];

void MakeDP() {
  dp[0] = dp[1] = 1;
  for (int i = 2; i <= N; i++) {
    if (vip[i - 1] || vip[i]) {
      dp[i] = dp[i - 1];
    } else {
      dp[i] = dp[i - 2] + dp[i - 1];
    }
  }
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int a;
    cin >> a;
    vip[a] = true;
  }
  MakeDP();
  cout << dp[N];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}