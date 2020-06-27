aaa = list()
def bubunwa(S, count, retsu):
    global s
    global n
    if count < n:
        for i in range(10):
            if i not in retsu:
                bubunwa(S+i,count+1,retsu+[i])
    else:
        if S == s:
            setRetsu = set(retsu)
            if setRetsu not in aaa:
                aaa.append(setRetsu)
while True:
    n, s = map(int, input().split())
    if n == 0 and s == 0:
        break
    if n > 4:
        n = 10-n
        s = 45 - s
    bubunwa(0,0,[])
    print(len(aaa))
    aaa = list()

