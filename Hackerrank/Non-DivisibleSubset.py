def nonDivisibleSubset(k, s):
    remainder_counts = [0] * k  
    for num in s:
        remainder_counts[num % k] += 1   
    max_subset_size = min(remainder_counts[0], 1) 
    for i in range(1, (k // 2) + 1):
        if i == k - i: 
            max_subset_size += min(remainder_counts[i], 1)
        else:
            max_subset_size += max(remainder_counts[i], remainder_counts[k - i])    
    return max_subset_size
n, k = 4, 3
s = [1, 7, 2, 4]
print(nonDivisibleSubset(k, s)) 
