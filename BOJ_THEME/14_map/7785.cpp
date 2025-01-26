#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
using namespace std;

int N;
unordered_map<string, bool> people;

void Solve() {
  cin >> N;
  while (N--) {
    string name, query;
    cin >> name >> query;

    if (query == "enter")
      people[name] = 1;
    else
      people[name] = 0;
  }

  vector<string> names;
  for (const auto& [name, isIn] : people)
    if (isIn) names.push_back(name);

  sort(all(names), greater<>());

  for (const string& name : names) cout << name << "\n";
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  Solve();
  return 0;
}