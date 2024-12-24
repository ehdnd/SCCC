#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int N;

ll pac(ll i) {
  if (i <= 1) return 1;
  return i * pac(i - 1);
}

void Solve() {
  cin >> N;
  cout << pac(N);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}