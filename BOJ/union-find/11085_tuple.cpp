#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int p, w, c, v;
int S[1010];
vector<tuple<int, int, int>> lines;

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
    lines.emplace_back(-w, st, ed);
  }
  memset(S, -1, sizeof(S));

  sort(all(lines));

  for (const auto& [w, st, ed] : lines) {
    Union(st, ed);
    if (Find(c) == Find(v)) {
      cout << -w;
      return;
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}