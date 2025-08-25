#include <bits/stdc++.h>
using namespace std;

int N;
map<string, int> A;

void Solve() {
  cin >> N;
  while (N--) {
    string a;
    cin >> a;
    A[a]++;
  }

  auto it = max_element(A.begin(), A.end(), [&](const auto &x, const auto &y) {
    if (x.second == y.second) {
      return x.first > y.first;
    }
    return x.second < y.second;
  });

  cout << it->first << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}