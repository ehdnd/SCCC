#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, ans;
vector<vector<ll>> A, B;
vector<ll> selected;

ll FindMex() {
  unordered_set<ll> s;
  for (ll val : selected) s.insert(val);

  ll ret = 0;
  while (s.count(ret)) ret++;
  return ret;
}

void Dfs(ll row) {
  if (row == N) {
    ll curr = FindMex();
    ans = max(ans, curr);
    return;
  }

  for (ll val : B[row]) {
    selected.push_back(val);
    Dfs(row + 1);
    selected.pop_back();
  }
}

void Solve() {
  cin >> N;

  A.clear();
  A.resize(N, vector<ll>(N, 0));
  B.clear();
  B.assign(N, vector<ll>());
  selected.clear();

  for (auto& row : A)
    for (auto& val : row) cin >> val;

  for (ll i = 0; i < N; ++i) {
    ll sum = 0;
    B[i].push_back(sum);

    for (ll j = N - 1; j >= 0; --j) {
      sum += A[i][j];
      if (sum > N) break;
      B[i].push_back(sum);
    }
  }

  ans = 0;
  Dfs(0);
  cout << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}