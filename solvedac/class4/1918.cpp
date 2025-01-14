#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

vector<string> S;

string Modify(vector<string>& stk) {
  string c = stk.back();
  stk.pop_back();
  string op = stk.back();
  stk.pop_back();
  string a = stk.back();
  stk.pop_back();

  return a + c + op;
}

void Solve() {
  string input;
  cin >> input;
  for (char c : input) S.push_back(string(1, c));

  while (1) {
    bool isPar = false, isMul = false, isPlus = false;

    for (string s : S) {
      if (s == "(")
        isPar = true;
      else if (s == "*" || s == "/")
        isMul = true;
      else if (s == "+" || s == "-")
        isPlus = true;
    }

    if (!isPar && !isMul && !isPlus) break;

    vector<string> stk;

    if (isPar) {
      bool isModi = false;
      for (string s : S) {
        stk.push_back(s);

        if (!isModi && s == ")") {
          isModi = true;
          stk.pop_back();
          string m = Modify(stk);
          stk.pop_back();
          stk.push_back(m);
        }
      }
      swap(stk, S);

    } else if (isMul) {
      bool flag = false;
      bool isModi = false;

      for (string s : S) {
        stk.push_back(s);

        if (flag && !isModi) {
          stk.push_back(Modify(stk));
          isModi = true;
        }
        if (s == "*" || s == "/") flag = true;
      }
      swap(stk, S);

    } else if (isPlus) {
      bool flag = false;
      bool isModi = false;

      for (string s : S) {
        stk.push_back(s);

        if (flag && !isModi) {
          isModi = true;
          stk.push_back(Modify(stk));
        }
        if (s == "+" || s == "-") flag = true;
      }
      swap(stk, S);
    }
  }

  for (string s : S) cout << s;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}