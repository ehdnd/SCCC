#define ll long long
#define INF 2e9
#include <bits/stdc++.h>
using namespace std;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
char board[1001][1001];
bool vis[1001][1001][2];
bool check[1001][1001];
vector<tuple<int, int>> temp;
vector<tuple<int, int, int, int>> seq;

int n, m;

void pri() {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cout << check[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

int main() {
  cin >> n >> m;
  queue<tuple<int, int>> fire;
  queue<tuple<int, int, int, int>> que;
  int ex = -1, ey = -1;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      cin >> board[i][j];
      if (board[i][j] == 'F') fire.push({i, j}), check[i][j] = 1;
      if (board[i][j] == 'S') que.push({i, j, 0, 0});
      if (board[i][j] == 'E') ex = i, ey = j;
    }
  }

  int ans = INF;
  while (!que.empty()) {
    // pri();
    temp.clear();
    while (!fire.empty()) {
      auto [x, y](fire.front());
      fire.pop();
      temp.push_back({x, y});
    }
    for (auto [x, y] : temp) {
      for (int d = 0; d < 4; d++) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
        if (board[nx][ny] == '1' || check[nx][ny]) continue;
        fire.push({nx, ny});
        check[nx][ny] = 1;
      }
    }

    seq.clear();
    while (!que.empty()) {
      auto [x, y, f, cnt](que.front());
      que.pop();
      seq.push_back({x, y, f, cnt});
    }
    for (auto [x, y, f, cnt] : seq) {
      if (x == ex && ey == y) {
        ans = min(ans, cnt);
      }
      for (int d = 0; d < 4; d++) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
        if (check[nx][ny]) continue;

        if (board[nx][ny] == '1') {
          if (f == 0 && vis[nx][ny][1] == 0) {
            vis[nx][ny][1] = 1;
            que.push({nx, ny, 1, cnt + 1});
          }
        } else if (vis[nx][ny][f] == 0) {
          vis[nx][ny][f] = 1;
          que.push({nx, ny, f, cnt + 1});
        }
      }
    }
  }
  if (ans == INF)
    cout << -1;
  else
    cout << ans;
}