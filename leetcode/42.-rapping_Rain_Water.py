def trap(height):
    if not height:
        return 0
    stack = []
    water_trapped = 0
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break           
            distance = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[top]
            water_trapped += distance * bounded_height
        stack.append(i)
    return water_trapped


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
