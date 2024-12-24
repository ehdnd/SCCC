#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N;

ll fib(ll i) {
  if (i == 0) return 0;
  if (i == 1) return 1;
  return fib(i - 2) + fib(i - 1);
}

void Solve() {
  cin >> N;
  cout << fib(N);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}