#include <bits/stdc++.h>

using namespace std;

vector<tuple<int, int, int, int>> arr;
int seq[101010];
bool vis[101010];

int main() {
  int n, k;
  cin >> n >> k;
  for (int i = 1; i <= k; i++) {
    int v, a, b;
    cin >> v >> a >> b;
    vis[v] = 1;
    arr.push_back({b - a + 1, v, a, b});
  }
  for (int i = 1; i <= n; i++) {
    if (vis[i]) continue;
    arr.push_back({n, i, 1, n});
  }

  sort(arr.begin(), arr.end());
  //   for (auto [f, v, a, b] : arr) cout << v << " " << a << " " << b << "\n";

  for (auto [f, v, a, b] : arr) {
    int idx = a;
    bool flag = 0;
    while (idx <= n) {
      if (seq[idx] == 0) {
        seq[idx] = v;
        flag = 1;
        break;
      }  
      idx++;
    }
    if (flag == 0) {
      cout << -1;
      exit(0);
    }
  }

  for (int i = 1; i <= n; i++) cout << seq[i] << " ";
}