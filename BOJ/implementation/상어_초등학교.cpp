#include <bits/stdc++.h>
#define x first
#define y second
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, Q;
vector<vector<int>> board, likes;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

void Solve() {
  cin >> N;
  Q = N * N;
  board.resize(N, vector<int>(N, 0));
  likes.resize(Q + 1, vector<int>(Q + 1, 0));

  while (Q--) {
    int a;
    cin >> a;
    for (int i = 0; i < 4; ++i) {
      int b;
      cin >> b;
      likes[a][b] = 1;
    }

    vector<int> best = {1, 1, N, N}, curr;

    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < N; ++c) {
        if (board[r][c]) continue;

        int c_l = 0, c_e = 0;

        for (int i = 0; i < 4; ++i) {
          int nr = r + dr[i];
          int nc = c + dc[i];
          if (!inRange(nr, nc)) continue;

          const int& b = board[nr][nc];
          if (!b) c_e++;
          if (likes[a][b]) c_l++;
        }

        curr = {-c_l, -c_e, r, c};

        if (curr < best) best = curr;
      }
    }

    board[best[2]][best[3]] = a;
  }

  int ans = 0;
  int plus[] = {0, 1, 10, 100, 1000};

  for (int r = 0; r < N; ++r) {
    for (int c = 0; c < N; ++c) {
      int a = board[r][c];
      int cnt = 0;

      for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (!inRange(nr, nc)) continue;

        const int& b = board[nr][nc];
        if (likes[a][b]) cnt++;
      }

      ans += plus[cnt];
    }
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}