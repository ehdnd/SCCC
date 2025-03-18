#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, cnt;
pii P;
vector<pii> pts, hull;

ll CCW(const pii &a, const pii &b, const pii &c) {
  return (ll)1 * (b.x - a.x) * (c.y - a.y) - (ll)1 * (b.y - a.y) * (c.x - a.x);
}

ll Dist(const pii &a, const pii &b) {
  ll dx = a.x - b.x;
  ll dy = a.y - b.y;
  return dx * dx + dy * dy;
}

void ConvexHull() {
  swap(pts[0], *min_element(all(pts)));

  sort(pts.begin() + 1, pts.end(), [&](const pii &a, const pii &b) {
    ll cw = CCW(pts[0], a, b);
    return cw != 0 ? cw > 0 : Dist(pts[0], a) < Dist(pts[0], b);
  });

  for (const auto &p : pts) {
    while ((int)hull.size() > 1 &&
           CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
      hull.pop_back();
    hull.push_back(p);
  }
}

bool isInside() {
  int sz = hull.size();
  for (int i = 0; i < sz; ++i) {
    int nxt = (i + 1) % sz;
    if (CCW(hull[i], hull[nxt], P) <= 0) return false;
  }
  return true;
}

void Solve() {
  cin >> N >> P.x >> P.y;
  pts.resize(N);
  for (auto &p : pts) cin >> p.x >> p.y;

  while ((int)pts.size() > 2) {
    ConvexHull();

    if (!isInside()) break;

    cnt++;

    for (auto &p : hull) {
      pts.erase(remove(all(pts), p), pts.end());
    }

    hull.clear();
  }

  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}