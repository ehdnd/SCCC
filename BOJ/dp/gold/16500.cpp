#include <bits/stdc++.h>
using namespace std;

string S;
int N;
vector<string> A;
bool dp[101];

void Solve() {
  cin >> S >> N;
  A.resize(N);
  for (auto& str : A) cin >> str;

  // dp[k] : k개 제작 가능? / k-1번 문자까지 제작 가능? [0, K)
  dp[0] = 1;

  int S_len = S.length();
  for (int i = 1; i <= S_len; i++) {
    for (const auto& str : A) {
      int str_len = str.length();
      if (str_len > i || !dp[i - str_len]) continue;

      // substr(pos=, size_t=)
      if (S.substr(i - str_len, str_len) == str) {
        dp[i] = true;
        break;
      }
    }
  }

  cout << dp[S_len];
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}