#include <bits/stdc++.h>
using namespace std;

int N, M;
int max_cnt;
string G[20];
bool visited[20][20], used[26];
int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

void BackTracking(int x, int y, int cur_cnt) {
  max_cnt = max(max_cnt, cur_cnt);
  visited[x][y] = 1;
  used[G[x][y] - 'A'] = 1;

  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (nx < 0 || nx > N - 1 || ny < 0 || ny > M - 1) continue;
    if (!used[G[nx][ny] - 'A']) BackTracking(nx, ny, cur_cnt + 1);
  }

  visited[x][y] = 0;
  used[G[x][y] - 'A'] = 0;
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++) cin >> G[i];

  BackTracking(0, 0, 1);

  cout << max_cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}