#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int MAX = 505;
const int INF = 1e9;

int N, M, S, D;
vector<pii> adj[MAX];
vector<pii> adj_bfs[MAX];
int dist[MAX];
unordered_set<int> isUsed[MAX];

void Init() {
  for (int i = 0; i < MAX; i++) {
    adj[i].clear();
    adj_bfs[i].clear();
    isUsed[i].clear();
  }
}

void Dijkstra() {
  priority_queue<pii> pq;
  fill(dist, dist + MAX, INF);

  dist[S] = 0;
  pq.emplace(0, S);

  while (!pq.empty()) {
    auto [d, curr] = pq.top();
    pq.pop();
    d = -d;

    if (dist[curr] < d) continue;

    for (const auto& [nxt, w] : adj[curr]) {
      if (isUsed[curr].count(nxt)) continue;

      if (dist[nxt] > dist[curr] + w) {
        dist[nxt] = dist[curr] + w;
        pq.emplace(-dist[nxt], nxt);
      }
    }
  }
}

void FindIncludedNodes() {
  queue<int> q;
  q.push(D);

  while (!q.empty()) {
    auto curr = q.front();
    q.pop();

    for (const auto& [px, w] : adj_bfs[curr]) {
      if (dist[px] + w == dist[curr]) {
        if (isUsed[px].count(curr)) continue;

        isUsed[px].insert(curr);
        q.push(px);
      }
    }
  }
}

void Solve() {
  cin >> S >> D;
  Init();
  for (int i = 0; i < M; i++) {
    int u, v, p;
    cin >> u >> v >> p;
    adj[u].emplace_back(v, p);
    adj_bfs[v].emplace_back(u, p);
  }

  Dijkstra();

  if (dist[D] == INF) {
    cout << -1 << "\n";  // 개행 ...
    return;
  }

  FindIncludedNodes();

  Dijkstra();

  if (dist[D] == INF) {
    cout << -1 << "\n";
    return;
  }

  cout << dist[D] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);

  while (1) {
    cin >> N >> M;
    if (N == 0 && M == 0) return 0;
    Solve();
  }

  return 0;
}