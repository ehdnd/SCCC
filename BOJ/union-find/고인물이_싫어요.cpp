#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, M, Q;
vector<int> adj[101010], tanks, vis;
vector<pii> cnts;

pii Find(int x) {
  if (vis[x] == 2) return cnts[x];

  vis[x] = 1;
  auto& [ow, nw] = cnts[x];

  for (const int& nx : adj[x]) {
    if (vis[nx] == 1) continue;

    const auto& [now, nnw] = Find(nx);
    ow += now;
    nw += nnw;
  }

  (tanks[x]) ? nw++ : ow++;
  vis[x] = 2;
  return cnts[x];
}

void Solve() {
  cin >> N >> M >> Q;
  cnts.resize(N, {0, 0});
  vis.resize(N, 0);
  tanks.resize(N, 0);
  for (int& x : tanks) cin >> x;

  while (M--) {
    int a, b;
    cin >> a >> b;
    a--, b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for (int i = 0; i < N; ++i) {
    if (vis[i] == 2) continue;
    cnts[i] = Find(i);
  }

  while (Q--) {
    int q;
    q--;
    cout << (cnts[q].first >= cnts[q].second) << "\n";
  }

  for (auto p : cnts) cout << p.first << " " << p.second << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}