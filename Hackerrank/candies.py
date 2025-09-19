

import sys

def min_candies(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


def main():
    data = sys.stdin.buffer.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    ratings = [int(next(it)) for _ in range(n)]

    print(min_candies(ratings))


if __name__ == "__main__":
    main()
