#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, K, L, t, dir;
vector<vector<int>> board;
bool isFin;

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

// 판단필요
inline bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

void Solve() {
  cin >> N >> K;
  board.resize(N, vector<int>(N, 0));

  queue<pii> q;
  q.emplace(0, 0);
  dir = 1;
  t = 0;

  board[0][0] = 1;

  while (K--) {
    int r, c;
    cin >> r >> c;
    r--, c--;
    board[r][c] = 2;
  }

  cin >> L;

  while (L--) {
    if (isFin) break;

    int X;
    char C;
    cin >> X >> C;

    int mv = X - t;

    while (mv--) {
      t++;

      auto [r, c] = q.back();
      int nr = r + dr[dir];
      int nc = c + dc[dir];

      if (!inRange(nr, nc) || board[nr][nc] == 1) {
        isFin = true;
        break;
      }

      q.emplace(nr, nc);

      if (board[nr][nc] == 2) {
        board[nr][nc] = 1;
        continue;
      }

      board[nr][nc] = 1;

      auto [er, ec] = q.front();
      q.pop();
      board[er][ec] = 0;
    }

    if (C == 'L') {
      dir = (dir + 3) % 4;
    } else {
      dir = (dir + 1) % 4;
    }
  }

  while (!isFin) {
    t++;
    auto [r, c] = q.back();
    int nr = r + dr[dir];
    int nc = c + dc[dir];

    if (!inRange(nr, nc) || board[nr][nc] == 1) {
      break;
    }

    q.emplace(nr, nc);

    if (board[nr][nc] == 2) {
      board[nr][nc] = 1;
    } else {
      board[nr][nc] = 1;
      auto [er, ec] = q.front();
      q.pop();
      board[er][ec] = 0;
    }
  }

  cout << t;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}