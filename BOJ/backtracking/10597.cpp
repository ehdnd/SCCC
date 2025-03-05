#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

string num;
bool isSol, vis[51];
int len;
vector<int> ans;

void BT(int idx) {
  if (isSol) return;

  if (idx == len) {
    for (int i = 1; i <= (int)ans.size(); ++i)
      if (!vis[i]) return;

    isSol = true;
    for (int& n : ans) cout << n << " ";
    return;
  }

  int a = num[idx] - '0';
  if (a == 0) return;

  if (!vis[a]) {
    vis[a] = 1;
    ans.push_back(a);
    BT(idx + 1);
    vis[a] = 0;
    ans.pop_back();
  }

  if (idx + 1 == len) return;

  int b = (num[idx] - '0') * 10 + (num[idx + 1] - '0');
  if (b > 50) return;

  if (!vis[b]) {
    vis[b] = 1;
    ans.push_back(b);
    BT(idx + 2);
    vis[b] = 0;
    ans.pop_back();
  }
}

void Solve() {
  cin >> num;
  len = num.length();
  BT(0);
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}