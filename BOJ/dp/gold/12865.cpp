#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int num_items, max_weight;
int profits[101], weights[101];
int dp[101][101010];

void FindSelectedItems() {
  int i = num_items;
  int j = max_weight;
  vector<int> selected;

  while (i > 0 && j > 0) {
    if (dp[i][j] != dp[i - 1][j]) {
      selected.push_back(i);
      j -= weights[i];
    }
    i--;
  }

  reverse(all(selected));
  for (auto item : selected) cout << item << " ";
}

void Solve() {
  cin >> num_items >> max_weight;

  for (int i = 1; i <= num_items; i++) cin >> weights[i] >> profits[i];

  for (int i = 0; i <= num_items; i++) {
    for (int w = 0; w <= max_weight; w++) {
      if (i == 0 || w == 0) {
        dp[i][w] = 0;
      } else if (weights[i] <= w) {
        dp[i][w] = max(profits[i] + dp[i - 1][w - weights[i]], dp[i - 1][w]);
      } else {
        dp[i][w] = dp[i - 1][w];
      }
    }
  }

  cout << dp[num_items][max_weight];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}