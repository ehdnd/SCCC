#include <bits/stdc++.h>
using namespace std;
using P = pair<int, int>;

const int INF = 1e9;
int N, E, V1, V2;
vector<P> graph[808];

vector<int> Dijkstra(int st) {
  vector<int> dist(N + 1, INF);
  priority_queue<P> pq;

  dist[st] = 0;
  pq.emplace(0, st);

  while (!pq.empty()) {
    auto [current_dist, current] = pq.top();
    pq.pop();
    current_dist = -current_dist;

    if (current_dist > dist[current]) continue;

    for (auto [next, weight] : graph[current]) {
      if (dist[next] > dist[current] + weight) {
        dist[next] = dist[current] + weight;
        pq.emplace(-dist[next], next);
      }
    }
  }
  return dist;
}

void Solve() {
  cin >> N >> E;
  for (int i = 0; i < E; i++) {
    int a, b, w;
    cin >> a >> b >> w;
    graph[a].emplace_back(b, w);
    graph[b].emplace_back(a, w);
  }
  cin >> V1 >> V2;

  vector<int> dist_st = Dijkstra(1);
  vector<int> dist_V1 = Dijkstra(V1);
  vector<int> dist_V2 = Dijkstra(V2);

  int r1 = dist_st[V1] + dist_V1[V2] + dist_V2[N];
  int r2 = dist_st[V2] + dist_V2[V1] + dist_V1[N];

  if (dist_st[V1] == INF || dist_V1[V2] == INF || dist_V2[N] == INF) r1 = INF;
  if (dist_st[V2] == INF || dist_V2[V1] == INF || dist_V1[N] == INF) r2 = INF;

  int res = min(r1, r2);
  if (res >= INF) {
    cout << -1;
  } else {
    cout << res;
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}