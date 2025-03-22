#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;

int N;
vector<ll> A, B, C, D, L, R;

void Solve() {
  cin >> N;
  A.resize(N);
  B.resize(N);
  C.resize(N);
  D.resize(N);

  for (int i = 0; i < N; ++i) cin >> A[i] >> B[i] >> C[i] >> D[i];

  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) {
      L.push_back(A[i] + B[j]);
      R.push_back(C[i] + D[j]);
    }

  sort(all(L));
  sort(all(R));

  ll ans = 0;

  for (const ll& l : L)
    ans += upper_bound(all(R), -l) - lower_bound(all(R), -l);

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}