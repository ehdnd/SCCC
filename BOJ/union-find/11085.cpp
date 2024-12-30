#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

struct Line {
  int st, ed, width;

  Line(int st, int ed, int width) : st(st), ed(ed), width(width) {}

  bool operator<(const Line& other) const { return width > other.width; }
};

int p, w, c, v;
int S[1010];
vector<Line> lines;

int Find(int a) {
  if (S[a] < 0) return a;
  return (S[a] = Find(S[a]));
}

bool Union(int a, int b) {
  a = Find(a);
  b = Find(b);
  if (a == b) return false;
  if (S[a] > S[b]) swap(a, b);
  S[a] += S[b];
  S[b] = a;
  return true;
}

void Solve() {
  cin >> p >> w >> c >> v;
  for (int i = 0; i < w; i++) {
    int st, ed, w;
    cin >> st >> ed >> w;
    lines.emplace_back(st, ed, w);
    // lines.push_back({st, ed, w}); // 구조체 생성자 없이 가능
  }
  memset(S, -1, sizeof(S));

  sort(all(lines));

  int res = 0;
  for (const auto& [st, ed, w] : lines) {
    if (Union(st, ed)) res = w;
    if (Find(c) == Find(v)) break;
  }
  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}