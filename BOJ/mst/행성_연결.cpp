#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, S[1010];
vector<tuple<int, int, int>> lines;

void Solve() {
  fill(S, S + 1010, -1);

  cin >> N;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      int a;
      cin >> a;
      if (i == j) continue;
      lines.emplace_back(a, i, j);
    }
  }
  sort(all(lines));

  auto Find = [&](int a, auto &&self) -> int {
    return S[a] < 0 ? a : S[a] = self(S[a], self);
  };
  auto Union = [&](int a, int b) -> bool {
    a = Find(a, Find);
    b = Find(b, Find);
    if (a == b) return true;
    if (S[a] > S[b]) swap(a, b);
    S[a] += S[b];
    S[b] = a;
    return false;
  };

  ll ans = 0;
  for (auto [a, b, c] : lines) {
    if (Union(b, c)) continue;
    ans += a;
  }
  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}