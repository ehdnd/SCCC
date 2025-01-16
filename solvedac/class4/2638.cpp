#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;
int N, M;
int day, cnt;
int curr_G[MAX][MAX], next_G[MAX][MAX], V[MAX][MAX];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

inline bool chk(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

void PaintOutside(int x, int y) {
  cnt++;
  curr_G[x][y] = 2;

  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];

    if (chk(nx, ny) && curr_G[nx][ny] == 0) {
      PaintOutside(nx, ny);
    }
  }
}

void MeltCheese(int x, int y) {
  V[x][y] = 1;

  int cnt_outside = 0;

  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];

    if (!chk(nx, ny)) continue;

    if (curr_G[nx][ny] == 2) cnt_outside++;
    if (curr_G[nx][ny] == 1 && !V[nx][ny]) MeltCheese(nx, ny);
  }

  if (cnt_outside >= 2)
    next_G[x][y] = 2;
  else
    next_G[x][y] = 1;
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> curr_G[i][j];
      next_G[i][j] = curr_G[i][j];
    }
  }

  while (1) {
    PaintOutside(0, 0);
    if (cnt == N * M) break;

    cnt = 0;
    memset(V, 0, sizeof(V));

    day++;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (curr_G[i][j] == 1 && !V[i][j]) MeltCheese(i, j);
      }
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (next_G[i][j] == 2) {
          curr_G[i][j] = 0;
          continue;
        }
        curr_G[i][j] = next_G[i][j];
      }
    }
  }

  cout << day;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}