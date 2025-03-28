#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;

int C;
vector<pii> pts;

int CCW(const pii& a, const pii& b, const pii& c) {
  int res = (b.x - a.x) * (c.y - a.y);
  res -= (b.y - a.y) * (c.x - a.x);
  return (res > 0) - (res < 0);
}

int D1(const pii& a, const pii& b) {
  int dx = a.x - b.x;
  int dy = a.y - b.y;
  return dx * dx + dy * dy;
}

ld D2(const pii& a, const pii& b) { return hypotl((b.x - a.x), (b.y - a.y)); }

void Solve() {
  cin >> C;
  pts.resize(C);
  for (auto& p : pts) cin >> p.x >> p.y;

  swap(pts[0], *min_element(all(pts)));
  sort(pts.begin() + 1, pts.end(), [&](const pii& a, const pii& b) {
    int cw = CCW(pts[0], a, b);
    return cw ? cw > 0 : D1(pts[0], a) < D1(pts[0], b);
  });

  vector<pii> hull;
  for (const auto& p : pts) {
    while ((int)hull.size() > 1 &&
           CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
      hull.pop_back();
    hull.push_back(p);
  }

  ld ans = -1;
  int sz = hull.size();

  for (int i = 0; i < sz; ++i) {
    for (int j = 0; j < sz; ++j) {
      ans = max(ans, D2(hull[i], hull[j]));
    }
  }

  cout << fixed << setprecision(9) << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}