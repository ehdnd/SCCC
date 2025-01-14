#include <bits/stdc++.h>
using namespace std;

// 차량기지 알고리즘

string S, ans;
vector<char> stk;

int GetPrecedence(char op) {
  if (op == '*' || op == '/') return 2;
  if (op == '+' || op == '-') return 1;
  return 0;
}

void Solve() {
  cin >> S;

  for (char c : S) {
    if (isupper(c)) {
      ans += c;

    } else if (c == '(') {
      stk.push_back(c);

    } else if (c == ')') {
      while (stk.back() != '(') {
        ans += stk.back();
        stk.pop_back();
      }
      stk.pop_back();

    } else {
      while (!stk.empty() && GetPrecedence(stk.back()) >= GetPrecedence(c)) {
        ans += stk.back();
        stk.pop_back();
      }
      stk.push_back(c);
    }
  }
  while (!stk.empty()) {
    ans += stk.back();
    stk.pop_back();
  }

  cout << ans;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}