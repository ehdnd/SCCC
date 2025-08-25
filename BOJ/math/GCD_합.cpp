#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

void Solve() {
  int N;
  cin >> N;
  vector<ll> A(N, 0);
  for (auto& x : A) cin >> x;

  ll ans = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      ans += gcd(A[i], A[j]);
    }
  }
  cout << ans << '\n';
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}