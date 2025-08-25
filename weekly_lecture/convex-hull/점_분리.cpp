#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, M;
vector<pii> blacks, whites;

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

vector<pii> ConvexHull(vector<pii>& pts) {
  vector<pii> hull;

  swap(pts[0], *min_element(all(pts)));

  sort(pts.begin() + 1, pts.end(), [&](const pii& a, const pii& b) {
    int cw = CCW(pts[0], a, b);
    return cw ? cw > 0 : Dist(pts[0], a) < Dist(pts[0], b);
  });

  for (auto& p : pts) {
  }

  return hull;
}

void Solve() {
  cin >> N >> M;
  blacks.resize(N);
  whites.resize(M);
  for (auto& p : blacks) cin >> p.x >> p.y;
  for (auto& p : whites) cin >> p.x >> p.y;

  vector<pii> b_hull = ConvexHull(blacks);
  vector<pii> w_hull = ConvexHull(whites);

  // 제작한 hull 두개에 대해 선분교차판정 해야한다.. HOW?
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) Solve();
  return 0;
}