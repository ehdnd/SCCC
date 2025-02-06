#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int D, N, res;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

struct Matrix {
  vector<int> board;
  int r, c;

  Matrix() : Matrix(0) {}

  Matrix(int size) {
    r = c = -1;
    board.resize(size * size, 0);
  }

  void MakeMatrix() {
    for (int i = 0; i < D; ++i) {
      for (int j = 0; j < D; ++j) {
        string val;
        cin >> val;
        int p = i * D + j;
        if (val == "X") {
          r = i, c = j;
          board[p] = -1;
        } else
          board[p] = stoi(val);
      }
    }
  }
};

inline bool inRange(int r, int c) { return 0 <= r && r < D && 0 <= c && c < D; }

void Solve() {
  Matrix st(D), ed(D);

  st.MakeMatrix();
  ed.MakeMatrix();

  res = INF;

  map<vector<int>, int> st_map, ed_map;

  queue<Matrix> q;
  st_map[st.board] = 0;
  q.push(st);

  for (int i = 0; i < N / 2; ++i) {
    int q_size = q.size();

    while (q_size--) {
      Matrix curr = q.front();
      q.pop();
      int r = curr.r, c = curr.c, p = r * D + c;

      for (int j = 0; j < 4; ++j) {
        int nr = r + dr[j], nc = c + dc[j], np = nr * D + nc;
        if (!inRange(nr, nc)) continue;

        swap(curr.board[p], curr.board[np]);
        if (!st_map.count(curr.board)) {
          curr.r = nr, curr.c = nc;
          st_map[curr.board] = i + 1;
          q.push(curr);
        }
        swap(curr.board[p], curr.board[np]);
      }
    }
  }

  queue<Matrix> qq;
  ed_map[ed.board] = 0;
  qq.push(ed);

  for (int i = 0; i < N / 2 + (N & 1); ++i) {
    int q_size = qq.size();

    while (q_size--) {
      Matrix curr = qq.front();
      qq.pop();
      int r = curr.r, c = curr.c, p = r * D + c;

      for (int j = 0; j < 4; ++j) {
        int nr = r + dr[j], nc = c + dc[j], np = nr * D + nc;
        if (!inRange(nr, nc)) continue;

        swap(curr.board[p], curr.board[np]);
        if (!ed_map.count(curr.board)) {
          curr.r = nr, curr.c = nc;
          ed_map[curr.board] = i + 1;
          qq.push(curr);
        }
        swap(curr.board[p], curr.board[np]);
      }
    }
  }

  for (const auto& [board, cnt] : st_map) {
    if (ed_map.count(board)) {
      res = min(res, cnt + ed_map[board]);
    }
  }

  if (res <= N) {
    cout << "SOLVABLE WITHIN " << res << " MOVES\n\n";
  } else {
    cout << "NOT SOLVABLE WITHIN " << N << " MOVES\n\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);

  string token;
  while (cin >> token) {
    cin >> D >> N;
    Solve();

    cin >> token;
  }
  return 0;
}