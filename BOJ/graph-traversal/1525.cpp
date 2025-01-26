#include <bits/stdc++.h>
using namespace std;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

struct Matrix {
  int board[3][3];
  int r, c;

  Matrix(int input_board[3][3]) {
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        board[i][j] = input_board[i][j];
        if (board[i][j] == 0) {
          r = i;
          c = j;
        }
      }
    }
  }

  bool operator<(const Matrix& other) const {
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        if (board[i][j] != other.board[i][j])
          return board[i][j] < other.board[i][j];
      }
    }
    return false;
  }

  bool operator==(const Matrix& other) const {
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        if (board[i][j] != other.board[i][j]) return false;
      }
    }
    return r == other.r && c == other.c;
  }
};

inline bool inRange(int r, int c) { return 0 <= r && r < 3 && 0 <= c && c < 3; }

void Solve() {
  int r, c, board[3][3];
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < 3; ++j) cin >> board[i][j];

  Matrix start(board);

  int temp[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
  Matrix ans(temp);

  set<Matrix> vis;
  queue<Matrix> q;
  q.push(start);
  vis.insert(start);

  int res = 0;

  while (!q.empty()) {
    int q_size = q.size();

    while (q_size--) {
      Matrix curr = q.front();
      q.pop();

      if (curr == ans) {
        cout << res;
        return;
      }

      Matrix nxt = curr;

      for (int i = 0; i < 4; i++) {
        int nr = curr.r + dr[i];
        int nc = curr.c + dc[i];

        if (!inRange(nr, nc)) continue;

        Matrix nxt = curr;
        swap(nxt.board[curr.r][curr.c], nxt.board[nr][nc]);
        nxt.r = nr;
        nxt.c = nc;

        if (vis.count(nxt)) continue;

        vis.insert(nxt);
        q.push(nxt);
      }
    }

    res++;
  }

  cout << -1;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}