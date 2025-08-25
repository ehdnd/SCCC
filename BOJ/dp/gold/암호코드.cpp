#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000;

vector<int> nums;
int dp[5000][2];

void Solve() {
  string tmp;
  cin >> tmp;
  for (char c : tmp) nums.push_back(c - '0');

  int len = (int)nums.size();
  if (nums[0]) dp[0][0] = 1;

  for (int i = 1; i < len; ++i) {
    if (nums[i] != 0) dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
    if (nums[i - 1] != 0 && nums[i - 1] * 10 + nums[i] <= 26)
      dp[i][1] = dp[i - 1][0];
  }

  cout << (dp[len - 1][0] + dp[len - 1][1]) % MOD;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}