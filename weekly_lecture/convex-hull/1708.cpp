#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;

struct Point {
  int x = 0, y = 0;
  int p = 1, q = 0;

  constexpr Point() = default;
  constexpr Point(int x, int y) : x(x), y(y) {}
  constexpr Point(int x, int y, int p, int q) : x(x), y(y), p(p), q(q) {}

  bool operator<(const Point& o) const {
    ll lhs = (ll)1 * q * o.p;
    ll rhs = (ll)1 * p * o.q;
    if (lhs != rhs) return lhs < rhs;
    if (y != o.y) return y < o.y;
    return x < o.x;
  }
};

ll CCW(const Point& a, const Point& b, const Point& c) {
  return (ll)1 * (b.x - a.x) * (c.y - a.y) - (ll)1 * (b.y - a.y) * (c.x - a.x);
}

int N;
vector<Point> points;

void Solve() {
  cin >> N;
  points.resize(N);
  for (auto& p : points) cin >> p.x >> p.y;

  sort(all(points));

  for (int i = 1; i < N; ++i) {
    points[i].p = points[i].x - points[0].x;
    points[i].q = points[i].y - points[0].y;
  }

  sort(points.begin() + 1, points.end());

  vector<int> s;
  s.push_back(0);
  s.push_back(1);

  for (int i = 2; i < N; ++i) {
    while ((int)s.size() >= 2) {
      int fi, se;
      fi = s.back();
      s.pop_back();
      se = s.back();

      if (CCW(points[se], points[fi], points[i]) > 0) {
        s.push_back(fi);
        break;
      }
    }
    s.push_back(i);
  }

  cout << s.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}