#include <bits/stdc++.h>
using namespace std;

const int MAX = 1010;

int N, M;
int graph[MAX][MAX], S[MAX * MAX];

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

inline bool inRange(int x, int y) { return 0 <= x && x < N && 0 <= y && y < M; }

inline int ToIndex(int r, int c) { return r * MAX + c; }

int Find(int a) { return (S[a] < 0 ? a : S[a] = Find(S[a])); }

bool Union(int a, int b) {
  a = Find(a);
  b = Find(b);
  if (a == b) return false;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return true;
}

void Solve() {
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    string row;
    cin >> row;
    for (int j = 0; j < M; j++) {
      graph[i][j] = row[j] - '0';
    }
  }
  fill(S, S + MAX * MAX, -1);

  for (int r = 0; r < N; ++r) {
    for (int c = 0; c < M; ++c) {
      int curr = ToIndex(r, c);
      if (graph[r][c]) continue;

      for (int i = 0; i < 4; ++i) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        if (inRange(nr, nc) && !graph[nr][nc]) {
          int adj = ToIndex(nr, nc);
          Union(curr, adj);
        }
      }
    }
  }

  for (int r = 0; r < N; ++r) {
    for (int c = 0; c < M; ++c) {
      int res = 0;
      int curr = ToIndex(r, c);
      unordered_set<int> used_pe;

      if (graph[r][c]) {
        for (int i = 0; i < 4; ++i) {
          int nr = r + dr[i];
          int nc = c + dc[i];
          if (!inRange(nr, nc) || graph[nr][nc]) continue;

          int adj = ToIndex(nr, nc);
          int pe = Find(adj);
          if (used_pe.count(pe)) continue;
          res += -S[pe];
          used_pe.insert(pe);
        }

        res++;
      }
      cout << res % 10;
    }
    cout << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}