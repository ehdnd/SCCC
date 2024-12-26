#include <bits/stdc++.h>
using namespace std;

int N, res;
string str;
int alpha[26];

bool chk(string str) {
  for (auto& i : alpha) i = -1;
  for (int i = 0; i < str.size(); i++) {
    char c = str[i];
    int ord = c - 'a';
    if (alpha[ord] != -1 && alpha[ord] != i - 1) return false;
    alpha[ord] = i;
  }
  return true;
}

void Solve() {
  cin >> N;
  while (N--) {
    cin >> str;
    if (chk(str)) res++;
  }
  cout << res;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}