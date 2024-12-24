#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

const int MAX = 101010;

int N, S, lo, hi, sum, cnt;
int nums[MAX];

void Solve() {
  cin >> N;
  hi = N - 1;
  for (int i = 0; i < N; i++) cin >> nums[i];
  cin >> S;

  sort(nums, nums + N);

  while (lo < hi) {
    sum = nums[lo] + nums[hi];
    if (sum == S) {
      lo++;
      hi--;
      cnt++;
    } else if (sum > S) {
      hi--;
    } else {
      lo++;
    }
  }
  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}