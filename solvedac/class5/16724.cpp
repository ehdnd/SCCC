#include <bits/stdc++.h>
using namespace std;

int N, M;
int S[1000 * 1000];

inline bool chk(int r, int c) { return 0 <= r && r < N && 0 <= c && c < M; }

int Find(int a) { return (S[a] < 0 ? a : S[a] = Find(S[a])); }

void Union(int a, int b) {
  a = Find(a), b = Find(b);
  if (a == b) return;
  S[a] += S[b];
  S[b] = a;
}

void Solve() {
  cin >> N >> M;
  memset(S, -1, sizeof(S));

  for (int r = 0; r < N; ++r) {
    string s;
    cin >> s;
    for (int c = 0; c < M; ++c) {
      char q = s[c];
      int nr, nc, np;

      if (q == 'D') {
        nr = r + 1, nc = c;
      } else if (q == 'L') {
        nr = r, nc = c - 1;
      } else if (q == 'R') {
        nr = r, nc = c + 1;
      } else {
        nr = r - 1, nc = c;
      }

      if (chk(nr, nc)) {
        int p = r * M + c;
        int np = nr * M + nc;
        Union(p, np);
      }
    }
  }

  int ans = 0;
  for (int i = 0; i < N * M; ++i)
    if (S[i] < 0) ans++;
  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}