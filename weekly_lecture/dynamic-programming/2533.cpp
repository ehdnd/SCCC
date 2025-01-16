#include <bits/stdc++.h>
using namespace std;

const int MAX = 1010101;
const int INF = 1e9;

int N;
vector<int> adj[MAX], child[MAX];
bool vis[MAX];
int dp[MAX][2];

void dfs(int curr) {
  vis[curr] = 1;
  for (const int& next : adj[curr]) {
    if (vis[next]) continue;

    child[curr].push_back(next);
    dfs(next);
  }
}

int SNS(int curr, bool pe) {
  int& ret = dp[curr][pe];
  if (ret != -1) return ret;

  int not_pick = INF, pick = 1;
  for (const int& next : child[curr]) {
    pick += SNS(next, true);
  }

  if (pe) {
    not_pick = 0;

    for (const int& next : child[curr]) {
      not_pick += SNS(next, false);
    }
  }

  return (ret = min(not_pick, pick));
}

void Solve() {
  cin >> N;
  for (int i = 0; i < N - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }

  dfs(0);

  memset(dp, -1, sizeof(dp));
  cout << SNS(0, true);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}