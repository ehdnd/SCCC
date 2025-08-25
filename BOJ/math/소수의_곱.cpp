#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MAX = 1LL << 31;

int K, N, cnt = 0;
vector<ll> P;
priority_queue<ll> pq;

void Solve() {
  cin >> K >> N;

  while (K--) {
    ll x;
    cin >> x;
    pq.push(-x);
    P.push_back(x);
  }

  ll p = -1;
  while (1) {
    ll x = pq.top();
    pq.pop();
    x *= -1;
    if (x == p) continue;
    p = x;
    cnt++;

    if (cnt == N) {
      cout << x;
      return;
    }

    for (const ll& p : P) {
      ll mul = x * p;
      if (mul < MAX) pq.push(-mul);
      // 중복 제거 최적화 로직을 기억하자.
      if (x % p == 0) break;
    }
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}