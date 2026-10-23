L = [2, 3, 5, 4, 8, 7,  1, 9, 6]

n = 0
for x in L:
   n = n + 1

for i in range(n):
   for j in range(n - 1):
    if L[j] > L[j + 1]:
      L[j] = L[j + 1]
      L[j + 1] = L[j]

print(L)