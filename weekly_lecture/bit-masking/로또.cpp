#include <bits/stdc++.h>
using namespace std;

void Solve() {
  while (1) {
    int K;
    cin >> K;
    if (!K) break;

    vector<int> nums(K);
    for (int& x : nums) cin >> x;

    for (int m = (1 << K) - 1; m >= 0; m--) {
      if (__builtin_popcount(m) != 6) continue;

      for (int i = K - 1; i >= 0; i--)
        if (m >> i & 1) cout << nums[K - 1 - i] << " ";

      cout << "\n";
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}
