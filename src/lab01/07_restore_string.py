interminal = input("in: ")
slovo = ""
index1 = 0
index2 = 0

for i in range(len(interminal)):
    if interminal[i].isupper():
        index1 = i
        break
    else:
        continue
for i in range(len(interminal)):
    if interminal[i] in "0123456789":
        index2 = i + 1
        break
    else:
        continue
shag = index2 - index1
for i in range(index1, len(interminal), shag):
    slovo += interminal[i]
print(f"out: {slovo}")
