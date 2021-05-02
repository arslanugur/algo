def read_and_rotate_matrix():
    m, n, r = [int(x) for x in input().strip().split()]
    F = [[(-1, -1)] * n for _ in range(m)]
    d0 = 2 * (m + n) - 4
    d = [d0 - (8 * x) for x in range(min(m, n) // 2)]
    A = [[0] * x for x in d]
    for i in range(m):
        v = [int(x) for x in input().strip().split()]
        for j in range(n):
            p = min(i, j, m - 1 - i, n - 1 - j)
            q = j - p if i == p\
                else (n - (3 * p) + i - 1 if j == n - 1 - p\
                      else (m + (2 * n) - (5 * p) - j - 3 if i == m - 1 - p\
                            else d0 - 7 * p - i))
            A[p][q] = v[j]
            F[i][j] = (p, q)
    for i in range(m):
        s = ""
        for j in range(n):
            p, q = F[i][j]
            print(s + str(A[p][(q + r) % d[p]]), end = "")
            s = " "
        print()

if __name__ == "__main__":
    read_and_rotate_matrix()
