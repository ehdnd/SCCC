#include <bits/stdc++.h>
using namespace std;

string sang_str;
string boom_str;

deque<char> S;
vector<char> R;

map<char, int> boom_to_idx;

void PopAndRes() {
  while (!S.empty()) {
    R.push_back(S.front());
    S.pop_front();
  };
}

void PopBoom() {
  int i = boom_str.length();
  while (i--) S.pop_back();
}

void Solve() {
  cin >> sang_str >> boom_str;

  if (boom_str.length() == 1) {
    for (char c : sang_str) {
      if (c == boom_str[0]) continue;
      R.push_back(c);
    }
    if (R.empty())
      cout << "FRULA";
    else
      for (auto c : R) cout << c;
    return;
  }

  for (int i = 0; i < boom_str.length(); i++) {
    boom_to_idx[boom_str[i]] = i;
  }

  for (const auto& c : sang_str) {
    S.push_back(c);

    if (c == boom_str[boom_str.length() - 1] && S.size() >= boom_str.size() &&
        boom_to_idx[S[S.size() - 2]] == boom_to_idx[c] - 1) {
      PopBoom();
      continue;
    }

    if (c == boom_str[0]) {
      continue;
    }

    if (S.size() >= 2 && boom_to_idx[S[S.size() - 2]] == boom_to_idx[c] - 1) {
      continue;
    }

    PopAndRes();
  }

  PopAndRes();

  if (R.empty())
    cout << "FRULA";
  else
    for (auto c : R) cout << c;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}

// abacabc
// abc
// 반례