#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Point {
  int x, y;
};

int N;
vector<Point> points;

ll CCW(const Point& a, const Point& b, const Point& c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) - 1LL * (b.y - a.y) * (c.x - a.x);
}

void Solve() {
  cin >> N;
  points.resize(N);
  for (auto& p : points) cin >> p.x >> p.y;

  int pivot_idx = 0;
  for (int i = 1; i < N; ++i) {
    if (points[i].y < points[pivot_idx].y ||
        points[i].y == points[pivot_idx].y && points[i].x < points[pivot_idx].x)
      pivot_idx = i;
  }
  swap(points[0], points[pivot_idx]);

  Point pivot = points[0];

  sort(points.begin() + 1, points.end(),
       [&pivot](const Point& a, const Point& b) {
         ll ori = CCW(pivot, a, b);

         if (ori == 0) {
           ll da = 1LL * (a.x - pivot.x) * (a.x - pivot.x) +
                   1LL * (a.y - pivot.y) * (a.y - pivot.y);
           ll db = 1LL * (b.x - pivot.x) * (b.x - pivot.x) +
                   1LL * (b.y - pivot.y) * (b.y - pivot.y);
           return da < db;
         }

         return ori > 0;
       });

  vector<Point> hull;
  hull.push_back(pivot);
  hull.push_back(points[1]);

  for (int i = 2; i < N; ++i) {
    while ((int)hull.size() >= 2 &&
           CCW(hull[hull.size() - 2], hull.back(), points[i]) <= 0)
      hull.pop_back();
    hull.push_back(points[i]);
  }

  cout << hull.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}