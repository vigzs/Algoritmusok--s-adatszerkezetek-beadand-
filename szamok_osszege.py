import sys
import bisect
import math

input = sys.stdin.read
data = input().splitlines()

A1, A2, A3 = map(int, data[0].split())
M = int(data[1])
B = list(map(int, data[2].split()))

H = math.gcd(math.gcd(A1, A2), A3)
T = [0]

for i in range(1, A1 * A2 + 1):
    if (i - A1 in T) or (i - A2 in T) or (i - A3 in T):
        T.append(i)

result = []
for j in range(M):
    if B[j] < A1 * A2:
        idx = bisect.bisect_left(T, B[j])
        result.append(T[idx])
    else:
        result.append((B[j] + H - 1) // H * H)

print(" ".join(map(str, result)))
