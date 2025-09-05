import math
def encryption(s):
    s = s.replace(" ", "")  
    length = len(s)
    rows = math.floor(math.sqrt(length))
    cols = math.ceil(math.sqrt(length))    
    if rows * cols < length:
        rows += 1    
    grid = [s[i:i+cols] for i in range(0, length, cols)]  
    encrypted = []
    for col in range(cols):
        encrypted.append("".join(row[col] for row in grid if col < len(row)))
    return " ".join(encrypted)
input_string = "have a nice day"
result = encryption(input_string)
print(result) 
