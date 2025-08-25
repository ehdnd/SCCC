#include <bits/stdc++.h>
using namespace std;

int N, M, K, size_max, curr_size;
int graph[101][101], vis[101][101];

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool chk(int r, int c) { return 0 <= r && r < N && 0 <= c && c < M; }

void Dfs(int r, int c) {
  vis[r][c] = 1;
  curr_size++;

  for (int i = 0; i < 4; i++) {
    int nr = r + dr[i];
    int nc = c + dc[i];

    if (!chk(nr, nc) || vis[nr][nc] || !graph[nr][nc]) continue;
    Dfs(nr, nc);
  }
}

void Solve() {
  cin >> N >> M >> K;
  for (int i = 0; i < K; i++) {
    int r, c;
    cin >> r >> c;
    graph[--r][--c] = 1;
  }

  for (int r = 0; r < N; r++) {
    for (int c = 0; c < M; c++) {
      if (graph[r][c] && !vis[r][c]) {
        curr_size = 0;
        Dfs(r, c);
        size_max = max(size_max, curr_size);
      };
    }
  }

  cout << size_max;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}