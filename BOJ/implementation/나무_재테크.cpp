#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N, M, K;
vector<vector<int>> A, C;
vector<vector<deque<int>>> B;

int dr[] = {1, -1, 0, 0, 1, -1, 1, -1};
int dc[] = {0, 0, 1, -1, 1, -1, -1, 1};

inline bool inRange(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }

void Solve() {
  cin >> N >> M >> K;
  A.resize(N, vector<int>(N, 5));
  B.resize(N, vector<deque<int>>(N));
  C.resize(N, vector<int>(N, 0));

  for (auto& r : C)
    for (int& x : r) cin >> x;

  while (M--) {
    int a, b, c;
    cin >> a >> b >> c;
    a--, b--;
    B[a][b].push_back(c);
  }

  for (auto& r : B)
    for (auto& d : r) sort(all(d));

  while (K--) {
    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < N; ++c) {
        deque<int> new_d, die_d, &cur_d = B[r][c];

        while (!cur_d.empty()) {
          int x = cur_d.front();

          if (x > A[r][c]) {
            while (!cur_d.empty()) {
              die_d.push_back(cur_d.front());
              cur_d.pop_front();
            }
            break;
          }

          A[r][c] -= x;
          new_d.push_back(x + 1);
          cur_d.pop_front();
        }

        cur_d.swap(new_d);

        while (!die_d.empty()) {
          int x = die_d.front();
          die_d.pop_front();
          A[r][c] += x / 2;
        }
      }
    }

    vector<vector<int>> adds(N, vector<int>(N, 0));
    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < N; ++c) {
        auto cur_d = B[r][c];
        while (!cur_d.empty()) {
          int x = cur_d.front();
          cur_d.pop_front();
          if (x && x % 5 == 0) {
            for (int k = 0; k < 8; ++k) {
              int nr = r + dr[k];
              int nc = c + dc[k];
              if (!inRange(nr, nc)) continue;
              adds[nr][nc]++;
            }
          }
        }
      }
    }
    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < N; ++c) {
        while (adds[r][c]--) {
          B[r][c].push_front(1);
        }
      }
    }

    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < N; ++c) {
        A[r][c] += C[r][c];
      }
    }
  }

  int ans = 0;
  for (int r = 0; r < N; ++r) {
    for (int c = 0; c < N; ++c) {
      ans += B[r][c].size();
    }
  }
  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}