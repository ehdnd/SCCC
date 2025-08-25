#include <bits/stdc++.h>
using namespace std;

int R, C;
vector<vector<int>> board;
vector<int> S;

int dr[] = {1, -1, 0, 0, 1, -1, 1, -1};
int dc[] = {0, 0, 1, -1, 1, -1, -1, 1};

inline bool inRange(int r, int c) { return 0 <= r && r < R && 0 <= c && c < C; }

int Find(int a) { return S[a] < 0 ? a : S[a] = Find(S[a]); }

bool Union(int a, int b) {
  a = Find(a), b = Find(b);
  if (a == b) return 0;
  S[a] += S[b];
  S[b] = a;
  return 1;
}

void Move(int p) {
  int r = p / C;
  int c = p % C;

  int max_i = -1;
  int min_b = board[r][c];

  for (int i = 0; i < 8; ++i) {
    int nr = r + dr[i];
    int nc = c + dc[i];
    if (!inRange(nr, nc)) continue;

    if (board[nr][nc] < min_b) {
      max_i = i;
      min_b = board[nr][nc];
    }
  }

  if (max_i == -1) return;

  int np = (r + dr[max_i]) * C + (c + dc[max_i]);

  if (!Union(np, p)) return;

  Move(np);
}

void Solve() {
  cin >> R >> C;
  board.resize(R, vector<int>(C, 0));
  for (auto& v : board)
    for (auto& x : v) cin >> x;

  S.resize(303030, -1);

  for (int i = 0; i < R * C; ++i) Move(i);

  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      int p = i * C + j;
      cout << (S[p] < 0 ? -S[p] : 0) << " ";
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}