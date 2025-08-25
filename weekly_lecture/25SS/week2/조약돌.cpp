#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

void Solve() {
  int N;
  cin >> N;
  vector<int> nums(N, 0);
  for (int& x : nums) cin >> x;

  int ans = 0;
  bool flag = 0;

  while (!flag) {
    flag = 1;

    int p = nums[0];

    for (int i = 1; i < N; ++i) {
      int c = nums[i];
      if (p && c) {
        int d = min(p, c);
        nums[i - 1] -= d;
        nums[i] -= d;
        flag = 0;
        ans++;
        break;
      }
      p = c;
    }
  }

  for (int& x : nums)
    if (x) ans++;

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}