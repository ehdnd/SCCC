#include <bits/stdc++.h>
using namespace std;

void Solve() {
  for (int T = 1;; ++T) {
    int N;
    cin >> N;
    if (N == 0) break;

    int ans = 0, cnt = 0;
    unordered_map<string, int> idx;
    vector<int> nxt(N, 0), vis(N, 0);

    for (int i = 0; i < N; ++i) {
      string a, b;
      cin >> a >> b;
      if (!idx.count(a)) idx[a] = cnt++;
      if (!idx.count(b)) idx[b] = cnt++;
      nxt[idx[a]] = idx[b];
    }

    auto Dfs = [&](auto&& self, int x) -> void {
      vis[x] = 1;
      if (!vis[nxt[x]]) self(self, nxt[x]);
    };

    for (int x = 0; x < N; ++x) {
      if (vis[x]) continue;
      Dfs(Dfs, x);
      ans++;
    }

    cout << T << " " << ans << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}