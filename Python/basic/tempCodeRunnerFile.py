# https://www.acmicpc.net/problem/10431 : 주사위 세개 (python3)
# 2023-09-17
# input 최적화 작업
from sys import stdin

input = stdin.readline

p = int(input())


def b_sort(arr):
    cnt = 0
    for i in range(1, 21):
        for j in range(i):
            if arr[i] < arr[j]:
                cnt += i - 1
                print(cnt, i - 1, j)
                arr.insert(j, arr[i])
                arr.pop(i + 1)
    return cnt


for _ in range(p):
    # 배열을 만들어서 하나씩 받아서 정렬함
    arr = list(map(int, input().split()))
    print(arr[0], b_sort(arr))
    print(arr)
