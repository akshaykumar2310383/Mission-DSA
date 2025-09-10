def sum_xor(n):
    count_zero_bits = 0
    while n > 0:
        if n & 1 == 0:  
            count_zero_bits += 1
        n >>= 1      
    return 2 ** count_zero_bits
n = int(input("Enter a number: "))
print(sum_xor(n))
