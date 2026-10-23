N = int(input("Entrez un entier superieur a zero (N) : "))
for i in range(1, N + 1):
    print("table de multiplication de ", i, ":")
    for j in range(1, 11):
        print(j, "x", i, "=", j * i)