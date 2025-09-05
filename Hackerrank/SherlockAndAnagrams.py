from collections import Counter
def sherlockAndAnagrams(s):   
    substrings = Counter()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):

            sorted_substring = ''.join(sorted(s[i:j]))
            substrings[sorted_substring] += 1
    anagram_pairs = 0
    for count in substrings.values():
        anagram_pairs += (count * (count - 1)) // 2 
    return anagram_pairs
s = "abba"
print(sherlockAndAnagrams(s)) 
