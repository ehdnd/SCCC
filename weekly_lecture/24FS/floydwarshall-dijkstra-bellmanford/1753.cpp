#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int V, E, K;
vector<pair<int, int>> graph[202020];
int dist[202020];

void Dijkstra() {
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
  dist[K] = 0;
  pq.emplace(0, K);

  while (!pq.empty()) {
    auto [current_dist, current] = pq.top();
    pq.pop();
    if (dist[current] < current_dist) continue;

    for (auto [next, weight] : graph[current]) {
      if (dist[next] > dist[current] + weight) {
        dist[next] = dist[current] + weight;
        pq.emplace(dist[next], next);
      }
    }
  }
}

void Solve() {
  cin >> V >> E;
  cin >> K;
  for (int i = 0; i < E; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    graph[u].emplace_back(v, w);
  }

  for (int i = 1; i <= V; i++) dist[i] = INF;
  Dijkstra();

  for (int i = 1; i <= V; i++) {
    if (dist[i] != INF)
      cout << dist[i] << "\n";
    else
      cout << "INF" << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}