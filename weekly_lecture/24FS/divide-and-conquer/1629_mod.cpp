#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll ModularPow(ll base, ll exp, const ll MOD) {
  ll res = 1;
  base %= MOD;
  while (exp) {
    if (exp & 1) res = (res * base) % MOD;

    base = (base * base) % MOD;
    exp = exp >> 1;
  }
  return res;
}

void Solve() {
  ll A, B, C;
  cin >> A >> B >> C;
  cout << ModularPow(A, B, C);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}