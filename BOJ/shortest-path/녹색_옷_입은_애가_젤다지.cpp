#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int N, T;
int board[125][125], dist[125][125];

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

void Solve() {
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j) {
      cin >> board[i][j];
      dist[i][j] = INF;
    }

  priority_queue<tuple<int, int, int>> pq;

  pq.emplace(-board[0][0], 0, 0);
  dist[0][0] = board[0][0];

  while (!pq.empty()) {
    auto [d, r, c] = pq.top();
    d *= -1;
    pq.pop();

    if (dist[r][c] < d) continue;

    for (int i = 0; i < 4; ++i) {
      int nr = r + dr[i];
      int nc = c + dc[i];
      if (!inRange(nr, nc)) continue;

      if (dist[nr][nc] > dist[r][c] + board[nr][nc]) {
        dist[nr][nc] = dist[r][c] + board[nr][nc];
        pq.emplace(-dist[nr][nc], nr, nc);
      }
    }
  }

  cout << "Problem " << T << ": " << dist[N - 1][N - 1] << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  while (1) {
    T++;
    cin >> N;
    if (N == 0) break;
    Solve();
  }
  return 0;
}