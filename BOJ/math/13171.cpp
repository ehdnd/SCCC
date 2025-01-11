#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1e9 + 7;
ll A, X;

void Solve() {
  cin >> A >> X;
  ll result = 1;
  A %= MOD;

  while (X) {
    if (X & 1) result = (result * A) % MOD;
    A = (A * A) % MOD;
    X >>= 1;
  }

  cout << result;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}