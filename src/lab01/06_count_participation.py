n_str = input()
n = int(n_str.strip())

ochno, zaochno = 0, 0

for _ in range(n):
    line = input().strip()
    if not line: continue
    parts = line.split()
    if parts[-1] == "True": ochno += 1
    else: zaochno += 1

print(ochno, zaochno)


