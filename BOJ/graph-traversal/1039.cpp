#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

string N;
int K, M;
unordered_set<string> vis;

void Solve() {
  cin >> N >> K;
  M = N.length();

  queue<string> q;
  q.push(N);

  while (K--) {
    int q_size = q.size();

    bool isPoss = false;
    vis.clear();

    while (q_size--) {
      string curr = q.front();
      q.pop();

      for (int i = 0; i < M; i++) {
        for (int j = i + 1; j < M; j++) {
          if (i == 0 && curr[j] == '0') continue;

          string nxt = curr;
          swap(nxt[i], nxt[j]);

          if (vis.find(nxt) != vis.end()) continue;

          vis.insert(nxt);
          q.push(nxt);
          isPoss = true;
        }
      }
    }

    if (!isPoss) {
      cout << -1;
      return;
    }
  }

  cout << *max_element(all(vis));
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}