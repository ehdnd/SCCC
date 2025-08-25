#include <bits/stdc++.h>
using namespace std;

int N;
int nums[202020], used_nums[10];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; ++i) cin >> nums[i];

  int var = 0, cnt = 0, lo = 0, hi = 0, ans = 0;

  while (1) {
    if (hi == N) break;

    if (var > 2) {
      if (!--used_nums[nums[lo]]) var--;
      lo++;
      cnt--;
    } else {
      if (!used_nums[nums[hi]]++) var++;
      hi++;
      cnt++;
    }

    if (var <= 2) ans = max(ans, cnt);
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}