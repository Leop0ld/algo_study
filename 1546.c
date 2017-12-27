#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getMax(int numArr[]);
float getAverage(float numArr[]);

int main() {
  char numberStr[100];
  int loop, maxNum, i = 0;

  scanf("%d\n", &loop);
  scanf(" %[^\n]s", numberStr);

  char* p = strtok(numberStr, " ");
  int numberArr[loop];
  float resultArr[loop];

  while (p != NULL) {
    numberArr[i++] = atoi(p);
    p = strtok(NULL, " ");
  }

  maxNum = getMax(numberArr);

  for(i = 0; i < loop; i++) {
    resultArr[i] = numberArr[i] / maxNum * 100;
  }

  printf("%.2f\n", getAverage(resultArr));

  return 0;
}

int getMax(int numArr[]) {
  int i, maxNum = numArr[0];
  int length = sizeof(*numArr) / sizeof(numArr[0]);

  for(i = 1; i < length; i++) {
    if(maxNum < i) maxNum = i;
  }

  return maxNum;
}

float getAverage(float numArr2[]) {
  float sum = 0.0;
  int i;
  int length = sizeof(*numArr2) / sizeof(numArr2[0]);

  for(i = 0; i < length; i++) {
    sum += numArr2[i];
  }

  return (float)sum/length;
}
