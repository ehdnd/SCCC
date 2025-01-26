#include <bits/stdc++.h>
using namespace std;

const int MAX = 1010;

int N, M, cnt, map_num;
int graph[MAX][MAX], vis[MAX][MAX];
unordered_map<int, int> map_count;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool inRange(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

void Dfs(int r, int c) {
  vis[r][c] = map_num;
  cnt++;

  for (int i = 0; i < 4; i++) {
    int nr = r + dr[i];
    int nc = c + dc[i];

    if (!inRange(nr, nc)) continue;

    if (!vis[nr][nc] && !graph[nr][nc]) {
      Dfs(nr, nc);
    }
  }
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    string row;
    cin >> row;
    for (int j = 0; j < M; j++) {
      graph[i][j] = row[j] - '0';
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (!vis[i][j] && !graph[i][j]) {
        cnt = 0;
        map_num++;
        Dfs(i, j);
        map_count[map_num] = cnt;
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      int res = 0;
      unordered_set<int> used_map_num;

      if (graph[i][j]) {
        for (int k = 0; k < 4; k++) {
          int nr = i + dr[k];
          int nc = j + dc[k];
          if (!inRange(nr, nc) || used_map_num.count(vis[nr][nc])) continue;

          res += map_count[vis[nr][nc]];
          used_map_num.insert(vis[nr][nc]);
        }
        res++;
      }

      cout << res % 10;
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}