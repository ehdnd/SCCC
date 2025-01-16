#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Point {
  ll x, y;

  Point() = default;
};

int N;
Point points[10101];
double res;

void CrossProduct(const Point& a, const Point& b) {
  Point base = points[0];

  ll x1 = a.x - base.x;
  ll x2 = b.x - base.x;
  ll y1 = a.y - base.y;
  ll y2 = b.y - base.y;

  res += x1 * y2 - y1 * x2;
}

void Solve() {
  cin >> N;
  for (auto& [x, y] : points) cin >> x >> y;

  for (int i = 1; i < N - 1; i++) CrossProduct(points[i], points[i + 1]);

  res = abs(res) / 2;
  cout << fixed << setprecision(1) << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}