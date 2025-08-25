#define ll long long
#include <bits/stdc++.h>
using namespace std;

ll arr[210101];
map<ll, ll> seq;

int main() {
  ll n, k;
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    cin >> arr[i];
  }

  seq[0] = 1;
  ll sum = 0;
  ll ans = 0;
  for (int i = 1; i <= n; i++) {
    sum += arr[i];
    if (seq.find(sum - k) != seq.end()) {
      ans += seq[sum - k];
    }
    // cout << sum << "\n";
    seq[sum]++;
  }
  cout << ans;
}
