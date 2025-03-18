n = int(input())
m = int(input())
mannaya = set()
for _ in range(n):
    mannaya.add(input())
ovsyanaya = set()
for _ in range(m):
    ovsyanaya.add(input())
common = mannaya & ovsyanaya
if common:
    print(len(common))
else:
    print("Таких нет")
