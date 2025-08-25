#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N, ans;
vector<pii> pts, idxs;
map<pii, int> floors;

int CCW(const pii& a, const pii& b, const pii& c) {
  int res = (b.x - a.x) * (c.y - a.y);
  res -= (b.y - a.y) * (c.x - a.x);
  return (res > 0) - (res < 0);
}

int dst(const pii& a, const pii& b) {
  int dx = a.x - b.x;
  int dy = a.y - b.y;
  return dx * dx + dy * dy;
}

void Solve() {
  cin >> N;
  pts.resize(N);
  idxs.resize(N);

  for (int i = 0; i < N; ++i) {
    pii& p = pts[i];
    cin >> p.x >> p.y;
    idxs[i] = p;
    floors[p] = 0;
  }

  while ((int)pts.size() > 2) {
    swap(pts[0], *min_element(all(pts)));

    sort(pts.begin() + 1, pts.end(), [&](const pii& a, const pii& b) {
      int cw = CCW(pts[0], a, b);
      return cw ? cw > 0 : dst(pts[0], a) < dst(pts[0], b);
    });

    vector<pii> hull;
    // 한 표지판이 다른 층의 꼭짓점이 아닌 경계에 위치할 수는 있다.
    for (const auto& p : pts) {
      while ((int)hull.size() > 1 &&
             CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
        hull.pop_back();
      hull.push_back(p);
    }

    ans++;

    if ((int)hull.size() < 3) break;

    for (auto& p : hull) {
      floors[p] = ans;
      pts.erase(remove(all(pts), p), pts.end());
    }

    hull.clear();
  }

  for (const auto& p : idxs) cout << floors[p] << " ";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}