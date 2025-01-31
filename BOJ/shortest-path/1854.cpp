#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, M, K;
vector<pii> adj[1010];

void Solve() {
  cin >> N >> M >> K;
  while (M--) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].emplace_back(b, c);
  }

  priority_queue<pii, vector<pii>, greater<pii>> pq;
  priority_queue<int> dist[1010];

  pq.emplace(0, 1);
  dist[1].push(0);

  while (!pq.empty()) {
    auto [w, x] = pq.top();
    pq.pop();

    if (dist[x].size() && dist[x].top() < w) continue;

    for (const auto& [nx, d] : adj[x]) {
      if (dist[nx].size() < K) {
        dist[nx].push(w + d);
        pq.emplace(w + d, nx);
      } else {
        if (dist[nx].top() > w + d) {
          dist[nx].pop();
          dist[nx].push(w + d);
          pq.emplace(w + d, nx);
        }
      }
    }
  }

  for (int i = 1; i <= N; ++i)
    cout << (dist[i].size() < K ? -1 : dist[i].top()) << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}