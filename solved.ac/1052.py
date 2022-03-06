# 백준 1052번 물병 68ms

'''
1. 지민 N개의 물병을 가지고 있음.
2. 각 물병에는 물을 무한대로 부을 수 있음
3. 모든 물병에는 물이 1리터씩 있음
4. 지민이는 한번에 K개의 물병을 옮길 수 있음
5. K 개를 넘지 않는 비어있지 않은 물병을 만든다!
6. 물의 재분배 규칙 : 같은 양의 물이 있는 물병 두개를 한쪽에 쏟아붙는걸 반복
7. 물이 부족할 시 물병을 하나 더 살 수 있다.

입력 : N, K
출력 : 상점에서 사야하는 물병의 최소값, 정답이 없으면 -1
'''
import sys

N, K = map(int, sys.stdin.readline().split())

buy = 0
while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    buy += 2**idx  #합치기 위해 필요한 최소 물의 양 구입
    N += 2**idx    #물을 합침
print(buy)