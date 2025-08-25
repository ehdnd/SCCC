#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N;
vector<int> nums;

ll Dist(int k) {
  ll res = 0;
  for (int i = 0; i < N; ++i) {
    res += abs((ll)1 * i * k - nums[i]);
  }
  return res;
}

void Solve() {
  cin >> N;
  nums.resize(N, 0);
  for (int& x : nums) cin >> x;

  ll lo = 0;
  ll hi = nums[N - 1];

  while (hi - lo >= 3) {
    ll p = (2 * lo + hi) / 3;
    ll q = (lo + 2 * hi) / 3;

    if (Dist(p) > Dist(q))
      lo = p;
    else
      hi = q;
  }

  ll res = 1e18;
  for (int i = lo; i <= hi; ++i) {
    res = min(res, Dist(i));
  }
  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}