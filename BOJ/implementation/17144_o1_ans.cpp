#include <bits/stdc++.h>
using namespace std;

int R, C, T;
int A[51][51];       // 현재 먼지 상태
int temp[51][51];    // 확산 결과 임시 저장
int airTop, airBot;  // 공기청정기 위치 (위쪽 행, 아래쪽 행)

// 4방향
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

bool inRange(int r, int c) { return (0 <= r && r < R && 0 <= c && c < C); }

void spreadDust() {
  // temp 배열 초기화
  memset(temp, 0, sizeof(temp));
  // 공기청정기 위치는 -1 유지
  temp[airTop][0] = -1;
  temp[airBot][0] = -1;

  // (1) 먼지가 있는 칸들만 큐에 넣는다
  queue<pair<int, int>> q;
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      if (A[r][c] > 0) q.push({r, c});  // 먼지 양이 양수인 칸
    }
  }

  // (2) 큐를 순회하면서 ‘현재 칸에서의 확산’을 1회 진행
  while (!q.empty()) {
    auto [r, c] = q.front();
    q.pop();

    int amount = A[r][c];
    int spreadAmount = amount / 5;
    if (spreadAmount == 0) {
      // 확산량이 0이면 퍼질 게 없으니 현재 칸 먼지만 더해주고 끝
      temp[r][c] += amount;
      continue;
    }

    int countSpread = 0;
    // 4방향 확산
    for (int i = 0; i < 4; i++) {
      int nr = r + dr[i];
      int nc = c + dc[i];
      // 맵 범위 안, 그리고 공기청정기 칸(-1)이 아닌 경우만 확산
      if (!inRange(nr, nc)) continue;
      if (nr == airTop && nc == 0) continue;  // 공기청정기 칸
      if (nr == airBot && nc == 0) continue;  // 공기청정기 칸

      temp[nr][nc] += spreadAmount;
      countSpread++;
    }
    // 남은 먼지는 = (원래 먼지) - (퍼진 횟수 × 확산량)
    temp[r][c] += (amount - spreadAmount * countSpread);
  }

  // (3) 확산 결과를 A로 복사
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      A[r][c] = temp[r][c];
    }
  }
}

void operateAirCleaner() {
  // 위쪽 공기청정기(반시계 방향)
  //  (1) 위쪽: 아래로 당김
  for (int r = airTop - 1; r > 0; r--) {
    A[r][0] = A[r - 1][0];
  }
  //  (2) 왼쪽 윗줄: 왼쪽으로 당김
  for (int c = 0; c < C - 1; c++) {
    A[0][c] = A[0][c + 1];
  }
  //  (3) 오른쪽 윗줄: 위로 당김
  for (int r = 0; r < airTop; r++) {
    A[r][C - 1] = A[r + 1][C - 1];
  }
  //  (4) 아래쪽 줄: 오른쪽으로 당김
  for (int c = C - 1; c > 1; c--) {
    A[airTop][c] = A[airTop][c - 1];
  }
  A[airTop][1] = 0;  // 공기청정기 옆은 항상 0

  // 아래쪽 공기청정기(시계 방향)
  //  (1) 아래쪽: 위로 당김
  for (int r = airBot + 1; r < R - 1; r++) {
    A[r][0] = A[r + 1][0];
  }
  //  (2) 왼쪽 아랫줄: 왼쪽으로 당김
  for (int c = 0; c < C - 1; c++) {
    A[R - 1][c] = A[R - 1][c + 1];
  }
  //  (3) 오른쪽 아랫줄: 아래로 당김
  for (int r = R - 1; r > airBot; r--) {
    A[r][C - 1] = A[r - 1][C - 1];
  }
  //  (4) 위쪽 줄: 오른쪽으로 당김
  for (int c = C - 1; c > 1; c--) {
    A[airBot][c] = A[airBot][c - 1];
  }
  A[airBot][1] = 0;  // 공기청정기 옆은 항상 0
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> R >> C >> T;

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      cin >> A[r][c];
      if (A[r][c] == -1) {
        // 공기청정기 위치 저장
        if (airTop == 0 && airBot == 0) {
          // 처음 발견된 -1
          airTop = r;
        } else {
          // 두 번째 발견된 -1
          airBot = r;
        }
      }
    }
  }

  while (T--) {
    spreadDust();         // (1) 미세먼지 확산
    operateAirCleaner();  // (2) 공기청정기 작동
  }

  // 남은 미세먼지 합 계산
  long long ans = 0;
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      if (A[r][c] > 0) ans += A[r][c];
    }
  }
  cout << ans << "\n";

  return 0;
}
