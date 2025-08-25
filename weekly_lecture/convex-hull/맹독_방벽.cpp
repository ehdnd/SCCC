#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, L;
double ans;
vector<pii> pts;

ll CCW(const pii& a, const pii& b, const pii& c) {
  ll res = (ll)1 * (b.x - a.x) * (c.y - a.y);
  res -= (ll)1 * (b.y - a.y) * (c.x - a.x);
  return (res > 0) - (res < 0);
}

ll D1(const pii& a, const pii& b) {
  ll dx = a.x - b.x;
  ll dy = a.y - b.y;
  return dx * dx + dy * dy;
}

double D2(const pii& a, const pii& b) {
  return hypot((b.x - a.x), (b.y - a.y));
}

void Solve() {
  cin >> N >> L;
  pts.resize(N);
  for (auto& p : pts) cin >> p.x >> p.y;

  swap(pts[0], *min_element(all(pts)));
  sort(pts.begin() + 1, pts.end(), [&](const pii& a, const pii& b) {
    ll cw = CCW(pts[0], a, b);
    return (cw ? cw > 0 : D1(pts[0], a) < D1(pts[0], b));
  });

  vector<pii> hull;
  for (auto& p : pts) {
    while ((int)hull.size() > 1 &&
           CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
      hull.pop_back();
    hull.push_back(p);
  }

  int sz = (int)hull.size();
  for (int i = 0; i < sz; ++i) {
    int nxt = (i + 1) % sz;
    ans += D2(hull[i], hull[nxt]);
  }
  ans += 2 * M_PI * L;

  //   cout << round(ans) << "\n";
  cout << fixed << setprecision(0) << ans << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}