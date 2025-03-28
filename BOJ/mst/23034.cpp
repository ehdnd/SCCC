#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using pii = pair<int, int>;

const int MAX = 1010;

int N, M, Q, max_w;
int S[MAX];
vector<tuple<int, int, int>> edges;
vector<pii> adj[MAX];

int Find(int a) { return (S[a] < 0 ? a : S[a] = Find(S[a])); }

bool Union(int a, int b) {
  a = Find(a), b = Find(b);
  if (a == b) return 0;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return 1;
}

bool Dfs(int p, int u, int ed) {
  if (u == ed) return true;

  for (const auto& [v, w] : adj[u]) {
    if (v == p) continue;
    if (Dfs(u, v, ed)) {
      max_w = max(max_w, w);
      return true;
    }
  }

  return false;
}

void Solve() {
  cin >> N >> M;
  while (M--) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.emplace_back(c, a, b);
  }

  sort(all(edges));
  memset(S, -1, sizeof(S));

  int mst = 0;
  for (const auto& [c, a, b] : edges) {
    if (Union(a, b)) {
      mst += c;
      adj[a].emplace_back(b, c);
      adj[b].emplace_back(a, c);
    }
    if (-S[Find(a)] == N) break;
  }

  cin >> Q;
  while (Q--) {
    int x, y;
    cin >> x >> y;
    max_w = 0;
    Dfs(-1, x, y);
    cout << mst - max_w << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}