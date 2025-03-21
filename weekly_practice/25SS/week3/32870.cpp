#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using pii = pair<int, int>;

const int INF = 1e9;
const int M = 3e5;

int N, Q;
vector<int> nums;
vector<pii> ans;

// 전처리르 하세요.

void Solve() {
  cin >> N >> Q;
  nums.resize(N, 0);
  ans.resize(M + 1, {0, 0});
  for (int& x : nums) cin >> x;

  sort(all(nums));

  const int MAX_NUM = nums.back();

  for (int m = 1; m <= M; ++m) {
    int min_a = INF;
    int max_a = 0;

    for (int k = 0; k * m <= MAX_NUM; ++k) {
      // 구간 [lo, hi]
      int lo = k * m;
      int hi = min(m * (k + 1) - 1, MAX_NUM);

      auto it1 = lower_bound(all(nums), lo);
      if (it1 == nums.end()) break;
      if (hi < *it1) continue;

      auto it2 = upper_bound(all(nums), hi);
      it2--;

      min_a = min(*it1 % m, min_a);
      max_a = max(*it2 % m, max_a);
    }

    ans[m] = {min_a, max_a};
  }

  while (Q--) {
    int q;
    cin >> q;
    cout << ans[q].first << " " << ans[q].second << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}