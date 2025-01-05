#include <bits/stdc++.h>
using namespace std;

string S, bomb;
string result;
int bomb_len;

void Solve() {
  cin >> S >> bomb;
  bomb_len = bomb.length();

  for (char c : S) {
    result.push_back(c);
    if (c == bomb.back() && result.size() >= bomb_len) {
      if (result.substr(result.size() - bomb_len, bomb_len) == bomb) {
        result.erase(result.size() - bomb_len, bomb_len);
      }
    }
  }

  if (result.empty())
    cout << "FRULA";
  else
    cout << result;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}