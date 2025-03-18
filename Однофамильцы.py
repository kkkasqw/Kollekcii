from collections import defaultdict

n = int(input())
surnames = [input() for _ in range(n)]
counts = defaultdict(int)

for surname in surnames:
    counts[surname] += 1

total = 0
for surname, cnt in counts.items():
    if cnt > 1:
        total += cnt

print(total)