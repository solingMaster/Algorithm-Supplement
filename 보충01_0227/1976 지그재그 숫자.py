# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
import sys
sys.stdin = open('1976 지그재그 숫자.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    s = 0
    for i in range(1,N+1):
        if i%2==1:
            s += i
        else:
            s -= i

    print(f"#{tc} {s}")