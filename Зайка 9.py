from collections import defaultdict

counts = defaultdict(int)
while True:
    line = input()
    if not line:
        break
    for obj in line.split():
        counts[obj] += 1
for obj, cnt in counts.items():
    print(f"{obj} {cnt}")