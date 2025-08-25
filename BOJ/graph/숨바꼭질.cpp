#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M;
vector<int> adj[20202];
bool vis[20202];

void Solve() {
  cin >> N >> M;
  while (M--) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }

  queue<int> q;
  int dist = -1;
  vector<int> nodes;

  vis[1] = 1;
  q.push(1);

  while (!q.empty()) {
    int q_size = q.size();

    nodes.clear();
    dist++;

    while (q_size--) {
      int cur = q.front();
      q.pop();
      nodes.push_back(cur);

      for (const int& nxt : adj[cur]) {
        if (vis[nxt]) continue;

        vis[nxt] = 1;
        q.push(nxt);
      }
    }
  }

  cout << *min_element(all(nodes)) << " " << dist << " " << nodes.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}