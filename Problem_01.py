X = []

L = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]

max_value = 0

def partialDigest(L):
    global X, max_value
    max_value = max(L)
    L.remove(max_value)
    X = [0, max_value]
    place(L, X)


def place(L, X):

    if not L:
        print("Result is:  ", X)
        return

    y = max(L)

    if Subset(y, X, L):
        X.append(y)
        removeElmnt(y, X, L)
        place(L, X)
        if y in X:
            X.remove(y)
        L.extend(Difference(y, X))

    if Subset(abs(max_value-y), X, L):
        X.append(abs(max_value-y))
        removeElmnt(abs(max_value-y), X, L)
        place(L, X)
        if abs(max_value-y) in X:
            X.remove(abs(max_value-y))
        L.extend(Difference(abs(max_value-y), X))

    return


def Difference(y, X):
    diff = []
    for i in X:
        diff.append(abs(y-i))
    return diff


def removeElmnt(y, X, L):
    for i in X:
        if abs(y - i) in L:
            L.remove(abs(y - i))


def Subset(y, X, L):
        for i in X:
            if abs(y-i) not in L:
                return False
        return True


def main():
    partialDigest(L)

main()
