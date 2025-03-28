#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;
using pii = pair<int, int>;

int N, res;
vector<pii> problems;

void Solve() {
  cin >> N;
  int max_day = N;

  while (N--) {
    int d, p;
    cin >> d >> p;
    problems.emplace_back(d, p);
  }
  sort(all(problems));

  priority_queue<int> pq;

  for (int i = max_day; i > 0; --i) {
    while (!problems.empty()) {
      auto [d, p] = problems.back();
      if (d < i) break;

      problems.pop_back();
      pq.push(p);
    }

    if (!pq.empty()) res += pq.top(), pq.pop();
  }

  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}