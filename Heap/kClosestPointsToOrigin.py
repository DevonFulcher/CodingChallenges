import math
import heapq
from typing import List

class Solution:
   
    def get_distance(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)
   
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_points = []
        for point in points:
            dis_points.append((self.get_distance(point), point[0], point[1]))
        heapq.heapify(dis_points)
        result = []
        for i in range(k):
            dis_point = heapq.heappop(dis_points)
            result.append((dis_point[1], dis_point[2]))
        return result