#include <bits/stdc++.h>
using namespace std;

int N;
vector<bool> isPrime;
vector<int> primes;

void MakePrimes() {
  isPrime.resize(N + 1, true);
  isPrime[0] = isPrime[1] = false;

  for (int num = 2; num * num <= N; num++) {
    if (isPrime[num]) {
      for (int i = num + num; i <= N; i += num) {
        isPrime[i] = false;
      }
    }
  }

  for (int i = 2; i <= N; ++i)
    if (isPrime[i]) primes.push_back(i);
}

void Solve() {
  cin >> N;

  MakePrimes();

  // [lo, hi)의 합 sum

  int lo = 0, hi = 0, sum = 0, ans = 0;
  int prime_cnt = primes.size();

  while (1) {
    if (sum >= N)
      sum -= primes[lo++];
    else if (hi == prime_cnt)
      break;
    else
      sum += primes[hi++];

    if (sum == N) ans++;
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}