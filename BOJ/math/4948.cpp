#include <bits/stdc++.h>
using namespace std;

const int MAX = 123456 * 2;

int N, sum;
vector<bool> p(MAX + 1);
vector<int> p_sum(MAX + 1);

void Solve() {
  p[2] = 1;
  for (int i = 3; i <= MAX; i += 2) p[i] = 1;
  for (int i = 3; i * i <= MAX; i += 2)
    if (p[i])
      for (int j = i * i; j <= MAX; j += 2 * i) p[j] = 0;

  for (int i = 1; i <= MAX; ++i) {
    if (p[i]) sum++;
    p_sum[i] = sum;
  }

  while (1) {
    cin >> N;
    if (!N) break;

    cout << p_sum[2 * N] - p_sum[N] << "\n";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}