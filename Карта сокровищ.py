def last_digit(x):
    return x % 10

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
groups = {}

for x, y in points:
    key = (last_digit(x), last_digit(y))
    if key not in groups:
        groups[key] = []
    groups[key].append((x, y))

max_count = 0
for key in groups:
    max_count = max(max_count, len(groups[key]))

print(max_count)