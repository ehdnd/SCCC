#include <bits/stdc++.h>

#define MAX 101010

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N, S;
int nums[101010];
int lo, hi, sum, len = MAX;

void Solve() {
  cin >> N >> S;
  for (int i = 0; i < N; i++) cin >> nums[i];

  while (1) {
    if (sum >= S) {
      len = min(len, hi - lo);
      sum -= nums[lo++];
    } else if (hi == N) {
      break;
    } else {
      sum += nums[hi++];
    }
  }
  cout << (len != MAX ? len : 0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}