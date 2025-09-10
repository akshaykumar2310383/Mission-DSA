from collections import defaultdict
def jim_and_the_jokes(n, jokes):
    remainder_count = defaultdict(int)
    joke_count = 0
    for h, m in jokes:
        total_minutes = h * 60 + m
        remainder = total_minutes % 60
        joke_count += remainder_count[remainder]
        remainder_count[remainder] += 1
    return joke_count
n = int(input())
jokes = [tuple(map(int, input().split())) for _ in range(n)]
print(jim_and_the_jokes(n, jokes))
