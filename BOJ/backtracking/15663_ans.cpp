#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
vector<int> nums, ans;
set<vector<int>> visited;

void BT(int num_cnt) {
  if (num_cnt == M) {
    for (int num : ans) cout << num << " ";
    cout << "\n";
    return;
  }

  int last_used = -1;
  for (int i = 0; i < N; i++) {
    if (nums[i] == last_used) continue;
    ans.push_back(nums[i]);
    BT(num_cnt + 1);
    ans.pop_back();
    last_used = nums[i];
  }
}

void Solve() {
  cin >> N >> M;
  nums.resize(N);
  for (int& num : nums) cin >> num;

  sort(all(nums));
  BT(0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}
