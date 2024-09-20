#include <stdio.h>
#define max 6

// conquer - 서열정리
void merge(int a[], int low, int mid, int high) {
  int b[100];
  int i = low;
  int j = mid + 1;
  int k = 0;

  // 한 쪽이 전멸할 때 까지 이간질 시작
  while (i <= mid && j <= high) {
    if (a[i] <= a[j]) {
      b[k] = a[i];
      k++;
      i++;
    } else {
      b[k] = a[j];
      k++;
      j++;
    }
  }

  // 전멸을 확인 - 왼쪽이 살아있다
  while (i <= mid) {
    b[k] = a[i];
    k++;
    i++;
  }
  // 오른쪽이 살아있다
  while (j <= high) {
    b[k] = a[j];
    k++;
    j++;
  }

  k--;
  // 문서작성 - 임시종이 b에서 진짜 종이로
  while (k >= 0) {
    a[low + k] = b[k];
    k--;
  }
}

// divide - 대진표 작성
void mergesort(int a[], int low, int high) {
  // exit condition

  if (low < high) {
    int m = (low + high) / 2;

    // left
    mergesort(a, low, m);

    // right
    mergesort(a, m + 1, high);

    //  fight
    merge(a, low, m, high);
  } else {
    return;
  }
}

int main() {
  int a[max] = {20, 10, 70, 80, 40, 90};
  int i = 0;

  printf("\n before merge");
  for (i = 0; i < max; i++) {
    printf(" %d", a[i]);
  }
  mergesort(a, 0, max - 1);

  printf("\n after merge");
  for (i = 0; i < max; i++) {
    printf(" %d", a[i]);
  }
}