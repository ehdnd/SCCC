#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

const int INF = 2e9;

int N;
vector<int> nums;

void Solve() {
  cin >> N;
  nums.resize(N, 0);
  for (int& num : nums) cin >> num;

  sort(all(nums));

  int lo = 0, hi = N - 1;
  int ans_a, ans_b, min_diff = INF;

  while (lo < hi) {
    int sum = nums[lo] + nums[hi];
    int curr_diff = abs(sum);

    if (curr_diff < min_diff) {
      min_diff = curr_diff;
      ans_a = nums[lo];
      ans_b = nums[hi];
    }

    (sum > 0) ? hi-- : lo++;
  }

  cout << ans_a << " " << ans_b << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}