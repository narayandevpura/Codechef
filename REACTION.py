t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    a = [[0] * c for _ in range(r)]

    flag = True

    for i in range(r):
        for j in range(c):
            a[i][j] = int(input())

    if a[0][0] > 1 | a[0][c - 1] > 1 | a[r - 1][0] > 1 | a[r - 1][c - 1] > 1:
        flag = False
        print("Unstable")
        continue

    if flag:
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if a[i][j] > 3:
                    flag = False
                    print("Unstable")
                    break
        if not flag:
            continue

    if flag:
        for i in [0, r - 1]:
            for j in range(1, c - 1):
                if a[i][j] > 2:
                    flag = False
                    print("Unstable")
                    break
        if not flag:
            continue

        if flag:
            for j in [0, c - 1]:
                for i in range(1, r - 1):
                    if a[i][j] > 2:
                        flag = False
                        print("Unstable")
                        break
            if not flag:
                continue

    if flag:
        print("Stable")
