#include <bits/stdc++.h>
using namespace std;

struct Point {
  int x, y, r;
};

int N;
int S[3030];
Point points[3030];

int Find(int a) {
  if (S[a] < 0) return a;
  return S[a] = Find(S[a]);
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

bool isConnected(int a, int b) {
  const auto& [x1, y1, z1] = points[a];
  const auto& [x2, y2, z2] = points[b];
  int dx = x1 - x2;
  int dy = y1 - y2;
  return dx * dx + dy * dy <= (z1 + z2) * (z1 + z2);
}

void Solve() {
  cin >> N;
  memset(S, -1, sizeof(S));
  //   memset(points, 0, sizeof(points));

  for (int i = 0; i < N; i++) {
    Point temp;
    cin >> temp.x >> temp.y >> temp.r;
    points[i] = temp;
  }

  for (int i = 0; i < N; i++)
    for (int j = i + 1; j < N; j++)
      if (isConnected(i, j)) Union(i, j);

  int res = 0;
  for (int i = 0; i < N; i++)
    if (S[i] < 0) res++;
  cout << res << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}