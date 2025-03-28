#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll INF = 3e9;

void Solve() {
  ll K;
  cin >> K;
  priority_queue<ll> pq_min, pq_max;
  unordered_map<ll, ll> nums;

  while (K--) {
    char q;
    ll n;
    cin >> q >> n;

    if (q == 'I') {
      pq_min.push(-n);
      pq_max.push(n);
      nums[n]++;
    } else {
      priority_queue<ll>& pq = (n == -1 ? pq_min : pq_max);

      while (1) {
        if (pq.empty()) break;

        ll x = pq.top();
        x *= n;
        if (!nums[x]) {
          pq.pop();
          continue;
        }

        nums[x]--;
        pq.pop();
        break;
      }
    }
  }

  ll ans[2] = {INF, INF};

  for (int i = 0; i < 2; ++i) {
    priority_queue<ll>& pq = (i == 0 ? pq_min : pq_max);

    while (1) {
      if (pq.empty()) break;

      ll x = pq.top();
      if (i == 0) x *= -1;

      if (!nums[x]) {
        pq.pop();
        continue;
      }

      ans[i] = x;
      break;
    }
  }

  if (ans[0] == INF)
    cout << "EMPTY";
  else
    cout << ans[1] << " " << ans[0];

  cout << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  ll T;
  cin >> T;
  while (T--) Solve();
  return 0;
}