#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> nums, ans, stk;

void Solve() {
  cin >> N;
  nums.resize(N, 0);
  ans.resize(N, -1);
  for (int& num : nums) cin >> num;

  for (int i = 0; i < N; ++i) {
    const int& num = nums[i];

    while (!stk.empty() && nums[stk.back()] < num) {
      ans[stk.back()] = num;
      stk.pop_back();
    }

    stk.push_back(i);
  }

  for (const int& num : ans) cout << num << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}