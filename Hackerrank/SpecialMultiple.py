from collections import deque
def find_special_multiple(n):
    queue = deque()
    queue.append("9")    
    while queue:
        current = queue.popleft()        
        num = int(current)     
        if num % n == 0:
            return current      
        queue.append(current + "0")
        queue.append(current + "9")
t = int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input("Enter value of N: "))
    print(find_special_multiple(n))
