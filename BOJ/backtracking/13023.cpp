#include <bits/stdc++.h>
using namespace std;

int N, M;

vector<int> adj[2020];
bool isPoss, vis[2020];

void Dfs(int cnt, int curr) {
  if (cnt == 5) {
    isPoss = true;
    return;
  }

  for (const int& nxt : adj[curr]) {
    if (isPoss) return;

    if (vis[nxt]) continue;

    vis[nxt] = 1;
    Dfs(cnt + 1, nxt);
    vis[nxt] = 0;
  }
}

void Solve() {
  cin >> N >> M;
  while (M--) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for (int i = 0; i < N; ++i) adj[N].push_back(i);

  Dfs(0, N);

  cout << isPoss;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}