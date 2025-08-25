#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N;
vector<int> A, ans;

void Solve() {
  cin >> N;
  A.resize(N, 0);
  for (auto& a : A) cin >> a;

  for (const int& num : A) {
    auto it = lower_bound(all(ans), num);

    if (it == ans.end()) {
      ans.push_back(num);
    } else {
      *it = num;
    }
  }

  cout << ans.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}