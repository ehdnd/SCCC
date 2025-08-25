#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

const int INF = 2e9 + 1;

int N;
vector<int> nums;

void Solve() {
  cin >> N;
  nums.resize(N, 0);
  for (int& num : nums) cin >> num;

  sort(all(nums));

  int min_diff = INF, a, b;
  int lo = 0, hi = N - 1;

  while (1) {
    if (lo == hi) break;

    int sum = nums[lo] + nums[hi];

    if (abs(sum) < min_diff) {
      min_diff = abs(sum);
      a = nums[lo];
      b = nums[hi];
    }

    if (sum > 0)
      hi--;
    else
      lo++;
  }

  cout << a << " " << b;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}