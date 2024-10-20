import sys

# Read input from standard input
N = int(sys.stdin.readline().strip())
fathers = [int(sys.stdin.readline().strip()) for _ in range(N - 1)]

s1 = []
s2 = []

for i in range(1, N):
    if fathers[i - 1] == 1:
        s1.append(i + 1)

level = 0

while s1:
    s2 = s1.copy()
    s1.clear()
    for i in range(1, N):
        if fathers[i - 1] in s2:
            s1.append(i + 1)
    level += 1

print(len(s2), level)
print(' '.join(map(str, s2)))
