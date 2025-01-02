#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, M;
int L1, L2, days;
vector<int> S;
int G[1500][1500];
int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
queue<pii> q_union, q_melt;

int Find(int a) {
  if (S[a] < 0) return a;
  return (S[a] = Find(S[a]));
}

bool Union(int a, int b) {
  a = Find(a);
  b = Find(b);
  if (a == b) return false;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return true;
}

inline bool Check(int a, int b) { return (0 <= a && a < N && 0 <= b && b < M); }

int To1D(int x, int y) { return x * M + y; }

void BfsUnion() {
  while (!q_union.empty()) {
    auto [x, y] = q_union.front();
    q_melt.push(q_union.front());
    q_union.pop();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (!Check(nx, ny) || !G[nx][ny]) continue;
      Union(To1D(x, y), To1D(nx, ny));
    }
  }
}

void BfsMelt() {
  while (!q_melt.empty()) {
    auto [x, y] = q_melt.front();
    q_melt.pop();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (!Check(nx, ny) || G[nx][ny]) continue;
      G[nx][ny] = 1;
      q_union.emplace(nx, ny);
    }
  }
}

void Solve() {
  cin >> N >> M;

  S.resize(N * M, -1);

  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < M; j++) {
      char c = s[j];
      if (c == '.') {
        G[i][j] = 1;
        q_union.emplace(i, j);
      } else if (c == 'X') {
        G[i][j] = 0;
      } else {
        G[i][j] = 2;
        q_union.emplace(i, j);
        if (!L1)
          L1 = To1D(i, j);
        else
          L2 = To1D(i, j);
      }
    }
  }

  while (1) {
    BfsUnion();
    if (Find(L1) == Find(L2)) break;
    BfsMelt();
    days++;
  }

  cout << days;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}