#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, L, R, T;
vector<vector<int>> board, vis;
bool flag;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

void Solve() {
  cin >> N >> L >> R;

  board.resize(N, vector<int>(N, 0));
  vis.resize(N, vector<int>(N, 0));

  for (auto& r : board)
    for (int& v : r) cin >> v;

  queue<pii> q, qq;

  while (1) {
    vis.assign(N, vector<int>(N, 0));
    flag = false;

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        if (vis[i][j]) continue;

        vis[i][j] = 1;
        q.emplace(i, j);
        qq.emplace(i, j);

        int cnt = 1;
        int sum = board[i][j];

        while (!q.empty()) {
          auto [r, c] = q.front();
          q.pop();

          int s = board[r][c];

          for (int dir = 0; dir < 4; ++dir) {
            int nr = r + dr[dir];
            int nc = c + dc[dir];

            if (!inRange(nr, nc) || vis[nr][nc]) continue;
            int ns = board[nr][nc];
            if (L > abs(s - ns) || R < abs(s - ns)) continue;

            vis[nr][nc] = 1;
            cnt++;
            sum += board[nr][nc];
            q.emplace(nr, nc);
            qq.emplace(nr, nc);
            flag = true;
          }
        }

        int each_sum = sum / cnt;

        while (!qq.empty()) {
          auto [r, c] = qq.front();
          qq.pop();

          board[r][c] = each_sum;
        }
      }
    }

    if (!flag) break;

    T++;
  }

  cout << T;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}