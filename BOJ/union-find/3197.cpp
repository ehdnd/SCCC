#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int N, M;
int L1, L2;
vector<int> S;
int G[1500][1500];
int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

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

bool Check(int a, int b) { return (0 <= a && a < N && 0 <= b && b < M); }

int ConverToS(int x, int y) { return x * M + y; }

void CheckAndUnion(int x, int y) {
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (!Check(nx, ny) || !G[nx][ny]) continue;
    Union(ConverToS(x, y), ConverToS(nx, ny));
  }
}

void InitializeG() {
  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < M; j++) {
      char c = s[j];
      if (c == '.')
        G[i][j] = 1;
      else if (c == 'X')
        G[i][j] = 0;
      else {
        G[i][j] = 2;
        if (!L1)
          L1 = ConverToS(i, j);
        else
          L2 = ConverToS(i, j);
      }
    }
  }
}

int Bfs() {
  queue<pii> q;
  int cnt = 0;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (!G[i][j]) continue;

      q.emplace(i, j);
      CheckAndUnion(i, j);
    }
  }
  if (Find(L1) == Find(L2)) return cnt;

  while (!q.empty()) {
    int q_size = q.size();
    cnt++;
    while (q_size--) {
      auto [x, y] = q.front();
      q.pop();

      for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (!Check(nx, ny) || G[nx][ny]) continue;

        G[nx][ny] = 1;
        CheckAndUnion(nx, ny);
        q.emplace(nx, ny);
      }
    }
    if (Find(L1) == Find(L2)) return cnt;
  }
  return -1;
}

void Solve() {
  cin >> N >> M;

  S.resize(N * M, -1);
  InitializeG();

  cout << Bfs();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}