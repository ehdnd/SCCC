#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// 왜틀림?
// 반례 2 4 5 같은놈들..

void Solve() {
  ll N, M, K;
  cin >> N >> M >> K;

  if (abs(N - M) > K || K > max(N, M)) {
    cout << -1 << "\n";
    return;
  }

  ll a, b, a_left, b_left;
  if (N > M) {
    a = 0, b = 1;
    a_left = N, b_left = M;
  } else {
    a = 1, b = 0;
    a_left = M, b_left = N;
  }

  for (ll i = 0; i < K; ++i) {
    cout << a;
    a_left--;
  }

  ll left = min(a_left, b_left);
  while (left--) {
    cout << b << a;
    a_left--;
    b_left--;
  }

  while (a_left--) cout << a;
  while (b_left--) cout << b;

  cout << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}