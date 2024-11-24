def main(name, n):
    if n == 0:
        return
    print(name)
    main(name, n - 1)

# main("chandan", 4)


def print1ton(count, n):
    if count == n:
        return
    print(count)
    print1ton(count - 1, n)

# print1ton(10, 1)


def sum(n, total, counter):
    if counter == n:
        return total + counter
    total += counter
    return sum(n, total, counter + 1)

print(sum(5, 0, 1))
    