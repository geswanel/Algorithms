# Solve system of linear equations
# ax + by = e
# cx + dy = f


# Cramer?
# x = d1 / d
# y = d2 / d

# a b | e
# c d | f
# d = ad - bc

# Solutions:
# 0. No solutions:            0
# 1. Infinity (y = kx + b):   1 k b
# 2. 1 solution:              2 x y
# 3. Infinity any y:          3 x
# 4. Infinity any x:          4 y
# 5. Any x y:                 5
eps = 1e-8


def det(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def linear_solve(a, b, ans):
    # ax + by = ans - solution
    if abs(a) < eps and abs(b) < eps and abs(ans) < eps:
        return 5, None, None
    elif abs(a) < eps and abs(b) < eps and abs(ans) >= 0:
        return 0, None, None
    else:
        if abs(a) < eps:
            return 4, ans / b, None
        elif abs(b) < eps:
            return 3, ans / a, None
        else:
            return 1, - a / b, ans / b


def zero_determinant(case1, a1, b1, case2, a2, b2):
    if case1 == case2 == 5:
        # Both infinity solutions => infinity solution
        return (5,)
    elif case1 == 0 or case2 == 0:
        # Any no solutions => no solutions
        return (0,)
    elif case1 == case2 == 3 or case1 == case2 == 4:
        # Both horizontal or both vertical
        if abs(a1 - a2) < eps:
            return (case1, a1)
        else:
            return (0,)
    elif case1 == case2 == 1:
        # both y = kx + b
        if abs(b1 - b2) < eps:
            return (case1, a1, b1)
        else:
            return (0,)
    elif case1 in (3, 4) and case2 == 5:
        return (case1, a1)
    elif case2 in (3, 4) and case1 == 5:
        return (case2, a2)
    elif case1 == 1:
        return (case1, a1, b1)
    else:
        return (case2, a2, b2)


def main():
    # a, b, e = (float(x) for x in input().split())
    # c, d, f = (float(x) for x in input().split())
    a, b, c, d, e, f = (float(input()) for _ in range(6))

    d0 = det(((a, b), (c, d)))
    if (abs(d0) >= eps):
        d1 = det(((e, b), (f, d)))
        d2 = det(((a, e), (c, f)))
        print(2, d1 / d0, d2 / d0)
    else:
        print(*zero_determinant(*linear_solve(a, b, e), *linear_solve(c, d, f)))


if __name__ == "__main__":
    main()