#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

ll DivideConquer(ll a, ll b) {
  if (b == 1) return a % C;

  ll half = DivideConquer(a, b / 2);

  if (b % 2 == 0)
    return half * half % C;
  else
    return (half * half % C) * a % C;
}

void Solve() {
  cin >> A >> B >> C;
  cout << DivideConquer(A, B);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}