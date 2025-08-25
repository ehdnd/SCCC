#include <bits/stdc++.h>
#define all(v) v.begin() v.end()
using namespace std;
using pii = pair<int, int>;

const int MAX = 101010;

int N, M, mst_cost, max_cost;
vector<pii> adj[MAX];
bool vis[MAX];

void Prim() {
  priority_queue<pii> pq;

  pq.emplace(0, 1);

  while (!pq.empty()) {
    auto [w, curr] = pq.top();
    pq.pop();
    w = -w;

    if (vis[curr]) continue;
    vis[curr] = 1;

    mst_cost += w;
    max_cost = max(max_cost, w);

    for (const auto& [nxt, cost] : adj[curr]) {
      if (vis[nxt]) continue;
      pq.emplace(-cost, nxt);
    }
  }
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].emplace_back(v, w);
    adj[v].emplace_back(u, w);
  }

  Prim();

  cout << mst_cost - max_cost;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}