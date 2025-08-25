#include <bits/stdc++.h>

using namespace std;

int N, ans;

int gcd(int a, int b) {
  if (a % b == 0) return b;
  return gcd(b, a % b);
}

int main() {
  cin >> N;
  for (int i = 2; i <= N; ++i) {
    for (int j = i + 1; j <= N; ++j) {
      if (gcd(j, i) == 1) ++ans;
    }
  }
  cout << ans;
}