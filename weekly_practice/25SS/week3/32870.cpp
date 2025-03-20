#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

const int INF = 1e9;

int N, Q;
vector<int> nums;

void Solve() {
  cin >> N >> Q;
  nums.resize(N, 0);
  for (int& x : nums) cin >> x;

  sort(all(nums));

  while (Q--) {
    int q;
    cin >> q;

    if (N == 1) {
      cout << nums[0] % q << "\n";
      continue;
    }

    int max_a = 0;
    int min_a = INF;
    int qm = q;

    for (int i = 2;; ++i) {
      auto it = lower_bound(all(nums), qm);

      if (it == nums.begin()) {
        max_a = max({max_a, *it % q, *(it + 1) % q});
        min_a = min({min_a, *it % q, *(it + 1) % q});
        qm = q * i;
        continue;
      }

      if (it == nums.end()) {
        max_a = max({max_a, *(it - 1) % q});
        min_a = min({min_a, *(it - 1) % q});
        break;
      }

      if (it == nums.end() - 1) {
        max_a = max({max_a, *it % q, *(it - 1) % q});
        min_a = min({min_a, *it % q, *(it - 1) % q});
        qm = q * i;
        continue;
      }

      max_a = max({max_a, *(it + 1) % q, *(it - 1) % q, *it % q});
      min_a = min({min_a, *(it + 1) % q, *(it - 1) % q, *it % q});

      qm = q * i;
    }

    cout << min_a << " " << max_a << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}