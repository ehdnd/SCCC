#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N;
int prev_max[3], now_max[3], prev_min[3], now_min[3];

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> now_max[j];
      now_min[j] = now_max[j];
      if (j == 1) {
        now_max[j] += max({prev_max[0], prev_max[1], prev_max[2]});
        now_min[j] += min({prev_min[0], prev_min[1], prev_min[2]});
      } else {
        now_max[j] += max({prev_max[j], prev_max[1]});
        now_min[j] += min({prev_min[j], prev_min[1]});
      }
    }
    for (int i = 0; i < 3; i++) {
      prev_max[i] = now_max[i];
      prev_min[i] = now_min[i];
    }
  }
  cout << max({prev_max[0], prev_max[1], prev_max[2]}) << " "
       << min({prev_min[0], prev_min[1], prev_min[2]});
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}