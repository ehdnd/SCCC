#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int R, C, T;
int robot_r1, robot_r2;
int curr_map[50][50], next_map[50][50];

inline bool CheckMapBoundary(int x, int y) {
  return 0 <= x && x < R && 0 <= y && y < C;
}

void Input() {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      int dust;
      cin >> dust;
      curr_map[i][j] = dust;
      if (dust < 0) {
        if (!robot_r1) {
          robot_r1 = i;
          robot_r2 = robot_r1 + 1;
        }
      }
    }
  }
}

void DustMove() {
  int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

  memset(next_map, 0, sizeof(next_map));
  next_map[robot_r1][0] = next_map[robot_r2][0] = -1;

  queue<pii> Q;

  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (curr_map[i][j] > 0) Q.emplace(i, j);
    }
  };

  while (!Q.empty()) {
    auto [x, y] = Q.front();
    Q.pop();

    int cnt = 0;
    int A = curr_map[x][y];

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i], ny = y + dy[i];
      if (!CheckMapBoundary(nx, ny) || curr_map[nx][ny] == -1) continue;

      cnt++;
      next_map[nx][ny] += A / 5;
    }

    next_map[x][y] += A - (A / 5) * cnt;
  }

  swap(curr_map, next_map);
}

void DustClean() {
  // 위쪽 공기청정기 (반시계 방향)
  for (int r = robot_r1 - 1; r > 0; r--) curr_map[r][0] = curr_map[r - 1][0];
  for (int c = 0; c < C - 1; c++) curr_map[0][c] = curr_map[0][c + 1];
  for (int r = 0; r < robot_r1; r++)
    curr_map[r][C - 1] = curr_map[r + 1][C - 1];
  for (int c = C - 1; c > 1; c--)
    curr_map[robot_r1][c] = curr_map[robot_r1][c - 1];
  curr_map[robot_r1][1] = 0;  // 공기청정기로 들어간 먼지 제거

  // 아래쪽 공기청정기 (시계 방향)
  for (int r = robot_r2 + 1; r < R - 1; r++)
    curr_map[r][0] = curr_map[r + 1][0];
  for (int c = 0; c < C - 1; c++) curr_map[R - 1][c] = curr_map[R - 1][c + 1];
  for (int r = R - 1; r > robot_r2; r--)
    curr_map[r][C - 1] = curr_map[r - 1][C - 1];
  for (int c = C - 1; c > 1; c--)
    curr_map[robot_r2][c] = curr_map[robot_r2][c - 1];
  curr_map[robot_r2][1] = 0;  // 공기청정기로 들어간 먼지 제거
}

int Result() {
  int res = 0;

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      int dust = curr_map[r][c];
      if (dust > 0) res += dust;
    }
  }

  return res;
}

void Solve() {
  cin >> R >> C >> T;
  Input();

  while (T--) {
    DustMove();
    DustClean();
  }

  cout << Result();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}
