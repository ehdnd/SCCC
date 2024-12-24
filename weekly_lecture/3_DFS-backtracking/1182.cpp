#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int n, s;
int nums[20];
int cnt, current_sum;

void BackTracking(int current) {
  if (current == n) return;
  if (current_sum + nums[current] == s) cnt++;

  // 선택안한채로
  BackTracking(current + 1);

  // 선택한채로
  current_sum += nums[current];
  BackTracking(current + 1);

  // 끝날 때 마다 방문 안한 상태로 돌려놓아야함
  current_sum -= nums[current];
}

void Solve() {
  cin >> n >> s;
  for (int i = 0; i < n; i++) cin >> nums[i];
  BackTracking(0);
  cout << cnt;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}