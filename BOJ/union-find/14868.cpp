#include <bits/stdc++.h>
using namespace std;

int N, K;
int S[101010];
int V[2020][2020];

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

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

bool CheckBound(int a, int b) { return (1 <= a && a <= N && 1 <= b && b <= N); }

void CheckAndUnion(int x, int y) {
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (!CheckBound(nx, ny) || !V[nx][ny]) continue;
    Union(V[x][y], V[nx][ny]);
  }
}

int Bfs() {
  queue<tuple<int, int, int>> Q;

  for (int i = 1; i <= K; i++) {
    int a, b;
    cin >> a >> b;
    V[a][b] = i;

    CheckAndUnion(a, b);
    if (-S[Find(V[a][b])] == K) return 0;

    Q.emplace(a, b, 1);
  }

  while (!Q.empty()) {
    auto [x, y, cnt] = Q.front();
    Q.pop();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (!CheckBound(nx, ny)) continue;

      if (!V[nx][ny]) {
        V[nx][ny] = V[x][y];
        Q.emplace(nx, ny, cnt + 1);
      }
      CheckAndUnion(nx, ny);  // 아 진짜 로 !...............
      if (-S[Find(V[x][y])] == K) return cnt;
    }
  }
  return -1;
}

void Solve() {
  cin >> N >> K;
  memset(S, -1, sizeof(S));
  cout << Bfs();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}