import heapq
class RunningMedian:
    def __init__(self):
        self.lower_half = []
        self.upper_half = []
    def add_number(self, num):
        heapq.heappush(self.lower_half, -num)
        if (self.lower_half and self.upper_half and 
            -self.lower_half[0] > self.upper_half[0]):
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
    def find_median(self):
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        return (-self.lower_half[0] + self.upper_half[0]) / 2
running_median = RunningMedian()
numbers = [5, 15, 1, 3]
for num in numbers:
    running_median.add_number(num)
    print(f"Added {num}, Running Median: {running_median.find_median()}")
