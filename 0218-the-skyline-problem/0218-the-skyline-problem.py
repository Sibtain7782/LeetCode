import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        heap = [(0, float('inf'))]
        result = []

        for x, neg_h, right in events:

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h != 0:
                heapq.heappush(heap, (neg_h, right))

            current_height = -heap[0][0]

            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result