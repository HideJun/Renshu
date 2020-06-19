A = list(map(str, input().split()))
B = dict()
for tango in A:
    if tango in B.keys():
        B[tango] += 1
    else:
        B[tango] = 1
MAX = 0
Ftango = str()
for i in B:
    if MAX < B[i]:
        MAX = B[i]
        Ftango = i
MAX = 0
Ltango = str()
for i in B:
    if MAX < len(i):
        MAX = len(i)
        Ltango = i
print(Ftango, Ltango)
