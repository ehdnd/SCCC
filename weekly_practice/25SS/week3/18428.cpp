#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

constexpr int S = 1;
constexpr int T = 2;
constexpr int O = 3;

int N;
bool isCaught;
vector<vector<int>> board;
vector<pii> teachers;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

void PaintBoard(int p, int val) { board[p / N][p % N] = val; }

bool isST(int p) { return board[p / N][p % N]; }

bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

bool Observe(int r, int c, int dir) {
  int nr = r + dr[dir];
  int nc = c + dc[dir];

  if (!inRange(nr, nc) || board[nr][nc] == O) return false;
  if (board[nr][nc] == S) return true;

  return Observe(nr, nc, dir);
}

void Solve() {
  cin >> N;
  board.resize(N, vector<int>(N, 0));

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      char a;
      int val = 0;
      cin >> a;
      if (a == 'S') {
        val = S;
      } else if (a == 'T') {
        val = T;
        teachers.emplace_back(i, j);
      }
      board[i][j] = val;
    }
  }

  for (int i = 0; i < N * N; ++i) {
    if (isST(i)) continue;
    PaintBoard(i, O);

    for (int j = i + 1; j < N * N; ++j) {
      if (isST(j)) continue;
      PaintBoard(j, O);

      for (int k = j + 1; k < N * N; ++k) {
        if (isST(k)) continue;
        PaintBoard(k, O);

        isCaught = false;

        for (const auto& [r, c] : teachers) {
          for (int dir = 0; dir < 4; ++dir) {
            isCaught |= Observe(r, c, dir);
          }

          if (!isCaught) {
            cout << "YES";
            return;
          }
        }

        PaintBoard(k, 0);
      }
      PaintBoard(j, 0);
    }
    PaintBoard(i, 0);
  }

  cout << "NO";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}