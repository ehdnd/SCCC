#include <bits/stdc++.h>
using namespace std;

const int MAX = 101010;

int N, cnt;
int S[MAX];
bool vis[MAX], fin[MAX];

void Initialize() {
  cnt = 0;
  fill(vis, vis + N, 0);
  fill(fin, fin + N, 0);
}

void Dfs(int curr) {
  vis[curr] = 1;
  int nxt = S[curr];

  if (vis[nxt]) {
    if (!fin[nxt]) {
      for (int temp = nxt; temp != curr; temp = S[temp]) cnt++;
      cnt++;
    }
  } else
    Dfs(nxt);

  fin[curr] = 1;
}

void Solve() {
  cin >> N;
  Initialize();
  for (int i = 0; i < N; i++) {
    cin >> S[i];
    S[i]--;
  };

  for (int node = 0; node < N; node++) {
    if (!vis[node]) Dfs(node);
  }
  cout << N - cnt << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}