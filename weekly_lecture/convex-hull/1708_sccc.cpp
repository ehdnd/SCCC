#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define x first
#define y second
using namespace std;
using ll = long long;
using pii = pair<int, int>;

int N;
vector<pii> P;

ll CCW(const pii &a, const pii &b, const pii &c) {
  return (ll)1 * (b.x - a.x) * (c.y - a.y) - (ll)1 * (b.y - a.y) * (c.x - a.x);
}

ll Dist(const pii &a, const pii &b) {
  ll dx = a.x - b.x;
  ll dy = a.y - b.y;
  return dx * dx + dy * dy;
}

void Solve() {
  cin >> N;
  P.resize(N);
  for (auto &p : P) cin >> p.x >> p.y;

  swap(P[0], *min_element(all(P)));

  sort(P.begin() + 1, P.end(), [&](const pii &a, const pii &b) {
    ll cw = CCW(P[0], a, b);
    return cw != 0 ? cw > 0 : Dist(P[0], a) < Dist(P[0], b);
  });

  vector<pii> hull;
  for (const auto &p : P) {
    while ((int)hull.size() > 1 &&
           CCW(hull[hull.size() - 2], hull.back(), p) <= 0)
      hull.pop_back();
    hull.push_back(p);
  }

  cout << hull.size();
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}