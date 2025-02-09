#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using ll = long long;
using namespace std;

const ll INF = 2e9;

void Solve() {
  ll N, M;
  cin >> N >> M;

  vector<ll> A(N, 0), B(M, 0);

  for (ll& a : A) cin >> a;
  for (ll& b : B) cin >> b;

  sort(all(B));

  bool flag = true;
  ll B_size = B.size();

  ll p = A[0];
  for (const ll& b : B) p = min(p, b - p);

  for (ll i = 1; i < N; ++i) {
    ll a = A[i];
    ll curr = (a >= p ? a : INF);

    ll lo = 0, hi = B_size - 1;

    while (lo <= hi) {
      ll mid = lo + (hi - lo) / 2;

      if (B[mid] - a >= p) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }

    if (0 <= lo && lo < B.size()) {
      curr = min(curr, B[lo] - a);
    } else if (curr == INF) {
      flag = false;
      break;
    }

    p = curr;
  }

  cout << (flag ? "YES" : "NO") << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  ll T;
  cin >> T;
  while (T--) Solve();
  return 0;
}