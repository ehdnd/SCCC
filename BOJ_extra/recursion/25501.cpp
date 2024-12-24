#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using p = pair<ll, ll>;

int cnt;

int recursion(const char *s, int l, int r) {
  cnt++;
  if (l >= r)
    return 1;
  else if (s[l] != s[r])
    return 0;
  else
    return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char *s) { return recursion(s, 0, strlen(s) - 1); };

void Solve() {
  char S[1001];
  cin >> S;
  cout << isPalindrome(S) << " " << cnt << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int T;
  cin >> T;
  while (T--) {
    cnt = 0;
    Solve();
  };
  return 0;
}