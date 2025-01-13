q = int(input())
s1 = []
s2 = []

for i in range(q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        s1.append(int(query[1]))
    elif t == 2:
        if not s2:
            while s1:
                s2.append(s1.pop())
        s2.pop()
    elif t == 3:
        if not s2:
            while s1:
                s2.append(s1.pop())
        print(s2[-1])
