#include <bits/stdc++.h>
using namespace std;

string S;
int used[26];

void Solve() {
  cin >> S;
  for (auto c : S) {
    used[tolower(c) - 'a']++;
  }

  int max_cnt = 0;
  vector<char> ans;

  for (int i = 0; i < 26; i++) {
    if (used[i] > max_cnt) {
      max_cnt = used[i];
      ans.clear();
      ans.push_back(i + 'a');
    } else if (used[i] == max_cnt) {
      ans.push_back(i + 'a');
    }
  }

  if (ans.size() == 1) {
    cout << (char)toupper(ans.front());
  } else {
    cout << "?";
  }
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}