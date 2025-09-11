s = input().strip()

letters = [(i, ch) for i, ch in enumerate(s) if ch.isalpha()]

p0 = None
for pos, (idx, ch) in enumerate(letters):
    if ch.isupper():
        p0 = pos
        break

result = ""
if p0 is not None:
    n_letters = len(letters)
    n = len(s)

    candidate_p1 = [pos for pos, (idx, _ch) in enumerate(letters) if idx - 1 >= 0 and s[idx - 1].isdigit()]

    found = False
    for p1 in candidate_p1:
        k = p1 - p0
        if k == 0:
            continue
        built_letters = []
        p = p0
        while 0 <= p < n_letters:
            idx, ch = letters[p]
            built_letters.append(ch)
            if idx + 1 < n and s[idx + 1] == ".":
                result = ("".join(built_letters)).lower() + "."
                found = True
                break
            p += k

        if found:
            break
    if not found:
        for p1 in candidate_p1:
            k = p1 - p0
            if k == 0:
                continue
            built_letters = []
            p = p0
            while 0 <= p < n_letters:
                idx, ch = letters[p]
                built_letters.append(ch)
                p += k
            if built_letters:
                result = ("".join(built_letters)).lower()
                break

print(result)


