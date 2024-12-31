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
  cout << "연결 " << a << " " << b << "\n";
  S[a] += S[b];
  S[b] = a;
  return true;
}

bool CheckBound(int a, int b) { return (1 <= a <= N && 1 <= b <= N); }

bool CheckConnected(int a, int b) {
  for (int i = 0; i < 4; i++) {
    int nx = a + dx[i];
    int ny = b + dy[i];
    if (!CheckBound(nx, ny)) continue;
    if (V[nx][ny] && V[nx][ny] != V[a][b]) return true;
  }
  return false;
}

void Solve() {
  cin >> N >> K;

  memset(S, -1, sizeof(S));
  queue<tuple<int, int, int>> Q;

  for (int i = 1; i <= K; i++) {
    int a, b;
    cin >> a >> b;
    V[a][b] = i;
    Q.emplace(a, b, 0);
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

        if (CheckConnected(nx, ny)) {
          Union(V[nx][ny], V[x][y]);
          if (-S[Find(V[x][y])] == K) {
            cout << cnt;
            return;
          }
        }
        Q.emplace(nx, ny, cnt + 1);
        continue;
      }

      if (V[nx][ny] == V[x][y]) continue;

      Union(V[nx][ny], V[x][y]);
      if (-S[Find(V[x][y])] == K) {
        cout << cnt;
        return;
      }
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}