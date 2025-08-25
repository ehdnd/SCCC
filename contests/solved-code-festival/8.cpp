#include <bits/stdc++.h>

using namespace std;

int N, ans;
int arr[10000];

int gcd(int a, int b) {
  int t = a % b;
  if (t == 0) return b;
  if (t != 2 && arr[t] == 1) return 1;
  return gcd(b, a % b);
}

int main() {
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(0);
  cin >> N;

  for (int i = 2; i <= 10000; i++) {
    if (arr[i] == 1) continue;
    int k = 2;
    int j = i;

    while (1) {
      j = i * k;
      if (j > 10000) break;
      arr[j] = 1;
      k++;
    }
  }

  for (int i = 2; i <= N; ++i) {
    for (int j = i + 1; j <= N; ++j) {
      if (gcd(i, j) == 1) {
        ++ans;
          }
    }
  }
  cout << ans;
}