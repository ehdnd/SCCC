#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using pii = pair<int, int>;

int N;
vector<pii> pts;

int CCW(const pii& a, const pii& b, const pii& c) {
  int res = (b.x - a.x) * (c.y - a.y);
  res -= (b.y - a.y) * (c.x - a.x);
  return (res > 0) - (res < 0);
}

int Dist(const pii& a, const pii& b) {
  int dx = a.x - b.x;
  int dy = a.y - b.y;
  return dx * dx + dy * dy;
}

int CrossProduct(const pii& a, const pii& b) { return a.x * b.y - a.y * b.x; }

void Solve() {
  cin >> N;
  pts.resize(N);
  for (auto& p : pts) cin >> p.x >> p.y;

  swap(pts[0], *min_element(all(pts)));

  sort(pts.begin() + 1, pts.end(), [&](const pii& a, const pii& b) {
    int cw = CCW(pts[0], a, b);
    return cw ? cw > 0 : Dist(pts[0], a) < Dist(pts[0], b);
  });

  vector<pii> hull;
  for (const auto& p : pts) {
    while ((int)hull.size() > 1 &&
           CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
      hull.pop_back();
    hull.push_back(p);
  }

  int sz = hull.size();
  int area = 0;
  for (int i = 0; i < sz; ++i)
    area += CrossProduct(hull[i], hull[(i + 1) % sz]);
  cout << area / 100;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}