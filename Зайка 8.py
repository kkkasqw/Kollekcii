n = int(input())
objects = set()
for _ in range(n):
    objects.update(input().split())
for obj in objects:
    print(obj)