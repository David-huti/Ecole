for i in range(2, 1001):
   PREMIER = True
   for j in range(2, i):
     if i % j == 0:
         PREMIER = False
     if PREMIER:
         print(i)