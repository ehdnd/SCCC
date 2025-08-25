#include <bits/stdc++.h>
using namespace std;

int N, M, P, cnt;
int S[101010], vis[101010];

bool Dfs(int curr) {
  vis[curr] = 1;
  int nxt = S[curr];
  if (!nxt) return true;

  if (vis[nxt]) return false;

  cnt++;
  return Dfs(nxt);
}

void Solve() {
  cin >> N >> M >> P;
  for (int i = 0; i < N; i++) {
    int u, v;
    cin >> u >> v;
    if (!S[v]) S[v] = u;
  }

  if (Dfs(P))
    cout << cnt;
  else
    cout << -1;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}