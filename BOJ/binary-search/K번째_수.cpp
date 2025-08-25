#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// https://st-lab.tistory.com/281

ll N, K;

bool isPoss(ll mid) {
  ll cnt = 0;
  for (int r = 1; r <= N; ++r) cnt += min(mid / r, N);
  return (cnt >= K);
}

void Solve() {
  cin >> N >> K;

  ll lo = 0, hi = 1e9;

  while (lo <= hi) {
    ll mid = lo + (hi - lo) / 2;
    if (isPoss(mid))
      hi = mid - 1;
    else
      lo = mid + 1;
  }

  cout << lo;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}