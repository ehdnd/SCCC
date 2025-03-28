#include <bits/stdc++.h>
using namespace std;

void Solve() {
  int N, M, Q;
  cin >> N >> M >> Q;

  vector<int> S(N, -1), tanks(N, 0);
  vector<vector<int>> cnts(2, vector<int>(N, 0));

  for (int& x : tanks) cin >> x;

  auto Find = [&](auto&& self, int a) -> int {
    return S[a] < 0 ? a : S[a] = self(self, S[a]);
  };

  auto Union = [&](int a, int b) -> bool {
    a = Find(Find, a);
    b = Find(Find, b);
    if (a == b) return false;
    if (S[a] > S[b]) swap(a, b);
    S[a] += S[b], S[b] = a;
    return true;
  };

  while (M--) {
    int a, b;
    cin >> a >> b;
    Union(--a, --b);
  }

  for (int i = 0; i < N; ++i) cnts[tanks[i]][Find(Find, i)]++;

  while (Q--) {
    int q;
    cin >> q;
    int p = Find(Find, --q);
    cout << (cnts[0][p] < cnts[1][p]) << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}