#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int INF = 1e9;
const int MAX = 10101;

int N, D, C;
int cnt, res;
vector<pii> graph[MAX];
int dist[MAX];

void Initialize() {
  cnt = 0;
  res = 0;
  for (int i = 0; i < MAX; i++) graph[i].clear();
}

void Dijkstra() {
  priority_queue<pii> pq;

  fill(dist, dist + MAX, INF);

  pq.emplace(0, C);
  dist[C] = 0;

  while (!pq.empty()) {
    auto [t, x] = pq.top();
    pq.pop();
    t = -t;
    if (dist[x] < t) continue;

    cnt++;
    res = dist[x];

    for (const auto& [nx, w] : graph[x]) {
      if (dist[nx] > dist[x] + w) {
        dist[nx] = dist[x] + w;
        pq.emplace(-dist[nx], nx);
      }
    }
  }
}

void Solve() {
  cin >> N >> D >> C;
  Initialize();

  while (D--) {
    int a, b, s;
    cin >> a >> b >> s;
    graph[b].emplace_back(a, s);
  }

  Dijkstra();

  cout << cnt << " " << res << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}