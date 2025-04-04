#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;
int N, M, day;
int G[MAX][MAX], V[MAX][MAX];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

inline bool chk(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

void PaintOutside(int x, int y) {
  G[x][y] = 2;
  V[x][y] = 1;

  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];

    if (chk(nx, ny) && G[nx][ny] != 1 && !V[nx][ny]) {
      PaintOutside(nx, ny);
    }
  }
}

bool MeltCheese() {
  vector<pair<int, int>> to_melt;

  // 그냥 for 문으로 처리하자
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (G[i][j] == 1) {
        int cnt_outside = 0;

        for (int k = 0; k < 4; k++) {
          int nx = i + dx[k];
          int ny = j + dy[k];

          if (G[nx][ny] == 2) cnt_outside++;
        }

        if (cnt_outside >= 2) to_melt.emplace_back(i, j);
      }
    }
  }

  for (const auto& [x, y] : to_melt) G[x][y] = 0;

  return (!to_melt.empty());
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++) cin >> G[i][j];

  while (1) {
    memset(V, 0, sizeof(V));
    PaintOutside(0, 0);
    if (!MeltCheese()) break;
    day++;
  }

  cout << day;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}