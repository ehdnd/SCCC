#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using ll = long long;
using namespace std;

const ll INF = 3e9;

ll N, ans_min;
vector<ll> nums, ans(3);

void Solve() {
  cin >> N;
  nums.resize(N);
  for (ll& num : nums) cin >> num;

  ans_min = INF;
  sort(all(nums));

  for (ll st = 0; st < N - 2; ++st) {
    ll lo = st + 1;
    ll hi = N - 1;

    while (lo < hi) {
      const ll &s = nums[st], &l = nums[lo], &h = nums[hi];
      ll sum = s + l + h;
      if (abs(sum) < ans_min) {
        ans_min = abs(sum);
        ans = {s, l, h};
      }

      (sum > 0) ? hi-- : lo++;
    }
  }

  for (const ll& n : ans) cout << n << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}