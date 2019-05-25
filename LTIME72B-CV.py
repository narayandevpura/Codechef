v = ['a','e','i','o','u']
t = int(input())
while t:
    n = int(input())
    s = input()
    f = 0
    if n > 1:
        for i in range(n-1):
            if s[i] not in v and s[i+1] in v:
                f = f + 1
    print(f)
    t = t-1