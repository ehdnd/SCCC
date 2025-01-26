#include <bits/stdc++.h>
using namespace std;

int N, M, day;
string graph[50];
bool vis[64][50][50];

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

inline bool inRange(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

void Solve() {
  cin >> N >> M;

  queue<tuple<int, int, int>> q;

  for (int i = 0; i < N; i++) {
    cin >> graph[i];
    for (int j = 0; j < M; j++) {
      if (graph[i][j] == '0') q.emplace(0, i, j);
    }
  };

  while (!q.empty()) {
    int q_size = q.size();
    day++;

    while (q_size--) {
      auto [key, x, y] = q.front();
      q.pop();

      for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        int nkey = key;

        if (!inRange(nx, ny)) continue;

        char& next_elem = graph[nx][ny];

        if (next_elem == '1') {
          cout << day;
          return;
        }

        else if (next_elem == '#')
          continue;

        else if (isupper(next_elem) && !(nkey & (1 << (next_elem - 'A'))))
          continue;

        else if (islower(next_elem))
          nkey |= (1 << (next_elem - 'a'));

        if (vis[nkey][nx][ny]) continue;

        vis[nkey][nx][ny] = 1;
        q.emplace(nkey, nx, ny);
      }
    }
  }

  cout << -1;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}