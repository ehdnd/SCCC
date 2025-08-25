#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, Q;
vector<int> adj[1010], cnts, vis;

bool Dfs(int x, int cnt, int ed) {
  vis[x] = 1;
  if (x == ed) {
    cnts[x] += cnt;
    return true;
  }

  for (int nx : adj[x]) {
    if (vis[nx]) continue;
    if (Dfs(nx, cnt + 1, ed)) {
      cnts[x] += cnt;
      return true;
    }
  }

  return false;
}

void Solve() {
  cin >> N;
  cnts.resize(N + 1, 0);
  vis.resize(N + 1, 0);

  N--;
  while (N--) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  cin >> Q;
  while (Q--) {
    int q;
    cin >> q;
    if (q == 1) {
      fill(all(vis), 0);
      int a, b;
      cin >> a >> b;
      Dfs(a, 0, b);
    } else {
      int x;
      cin >> x;
      cout << cnts[x] << "\n";
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}