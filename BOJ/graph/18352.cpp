#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M, K, X;
vector<int> adj[303030], ans;
vector<bool> vis;

void Solve() {
  cin >> N >> M >> K >> X;
  while (M--) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
  }

  vis.resize(N + 1, 0);

  queue<int> q;
  q.push(X);
  vis[X] = 1;

  while (K--) {
    int q_sz = q.size();

    while (q_sz--) {
      int x = q.front();
      q.pop();

      for (const int& nx : adj[x]) {
        if (vis[nx]) continue;
        vis[nx] = 1;
        q.push(nx);
      }
    }
  }

  if (q.empty()) {
    cout << -1;
    return;
  }

  while (!q.empty()) {
    ans.push_back(q.front());
    q.pop();
  }

  sort(all(ans));
  for (const int& x : ans) cout << x << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}