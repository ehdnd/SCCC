#define ll long long
#include <bits/stdc++.h>
using namespace std;

ll arr[101010];
ll brr[101010];
ll seqa[101010];
ll seqb[101010];

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> arr[i];
    seqa[arr[i]]++;
  }
  for (int i = 1; i <= n; i++) {
    cin >> brr[i];
    seqb[brr[i]]++;
  }

  sort(arr + 1, arr + 1 + n);
  sort(brr + 1, brr + 1 + n);
  for (int i = 1; i <= n; i++) {
    if (seqa[arr[i]] > 0 && seqb[arr[i]] > 0) {
      if (seqa[arr[i]] > seqb[arr[i]]) {
        seqa[arr[i]] -= seqb[arr[i]];
        seqb[arr[i]] = 0;
      } else {
        seqb[arr[i]] -= seqa[arr[i]];
        seqa[arr[i]] = 0;
      }
    }
  }

  int idxa = 1, idxb = 1;
  ll ans = 0;
  while (1) {
    if (idxa < n && seqa[arr[idxa]] == 0) {
      idxa++;
      continue;
    }
    if (idxb < n && seqb[brr[idxb]] == 0) {
      idxb++;
      continue;
    }
    ans += abs(arr[idxa] - brr[idxb]);
    // cout << idxa << " " << idxb << "\n";
    seqa[arr[idxa]]--;
    seqb[brr[idxb]]--;
    idxa++;
    idxb++;
    if (idxa > n || idxb > n) break;
  }
  cout << ans << "\n";
}