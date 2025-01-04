#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

const int INF = 1e9;
int N;
int G[101][101];
int new_map[101][101];
int V[101][101];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

queue<pii> qq;

inline bool CheckBound(int x, int y) {
  return 0 <= x && x < N && 0 <= y && y < N;
}

void PaintIsland(int cnt, int i, int j) {
  queue<pii> q;

  new_map[i][j] = cnt;
  V[i][j] = 1;
  q.emplace(i, j);

  while (!q.empty()) {
    auto [x, y] = q.front();
    qq.push(q.front());
    q.pop();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (!CheckBound(nx, ny) || new_map[nx][ny] || !G[nx][ny]) continue;

      new_map[nx][ny] = cnt;
      V[nx][ny] = 1;
      q.emplace(nx, ny);
    }
  }
}

int MakeBridge() {
  int res = INF;

  while (!qq.empty()) {
    int qq_size = qq.size();

    if (res != INF) return res;

    while (qq_size--) {
      auto [x, y] = qq.front();
      qq.pop();

      for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (!CheckBound(nx, ny)) continue;

        if (V[nx][ny] && new_map[nx][ny] != new_map[x][y]) {
          res = min(res, V[nx][ny] + V[x][y] - 2);
        }

        if (!V[nx][ny]) {
          new_map[nx][ny] = new_map[x][y];
          V[nx][ny] = V[x][y] + 1;
          qq.emplace(nx, ny);
        }
      }
    }
  }
  return -1;
}

void Solve() {
  cin >> N;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++) cin >> G[i][j];

  int cnt = 0;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      if (G[i][j] && !new_map[i][j]) PaintIsland(++cnt, i, j);

  cout << MakeBridge();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}