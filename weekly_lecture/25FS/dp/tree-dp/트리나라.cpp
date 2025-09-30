#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define prs(v)  \
  sort(all(v)); \
  v.erase(unique(all(v)), v.end())
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

const int MOD = 1e9 + 7;

int N, K;
vector<vector<ll>> adj, tree;
// dp[i][j][k]
// i 를 루트로 하는 서브트리에서
// j 번째 자식까지 고려한 (0 = non)
// k 개의 노드를 가지는 서브트리 경우의 수
ll dp[51][51][51];

void Tree(int u, int p) {
  for (int c : adj[u]) {
    if (c != p) {
      tree[u].push_back(c);
      Tree(c, u);
    }
  }
}

void Dfs(int u) {
  // base
  dp[u][0][1] = 1;

  for (int c : tree[u]) Dfs(c);

  for (int j = 1; j <= (int)tree[u].size(); ++j) {
    int c = tree[u][j - 1];

    for (int k = 1; k <= K; ++k) {
      dp[u][j][k] = dp[u][j - 1][k];

      for (int a = 1; a < k; ++a) {
        ll tmp = (dp[u][j - 1][k - a] * dp[c][(int)tree[c].size()][a]) % MOD;
        dp[u][j][k] = (dp[u][j][k] + tmp) % MOD;
      }
    }
  }
}

void Solve() {
  cin >> N >> K;
  adj.resize(N + 1);
  tree.resize(N + 1);

  for (int i = 0; i < N - 1; ++i) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  Tree(1, 0);
  Dfs(1);

  ll ans = 0;
  for (int i = 1; i <= N; ++i)
    ans = (ans + dp[i][(int)tree[i].size()][K]) % MOD;
  cout << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}