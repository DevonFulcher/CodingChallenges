class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        views = []
        peak = 0
        for i in range(len(heights)):
            opposite = len(heights)-1-i
            if heights[opposite] > peak:
                views.append(opposite)
                peak = heights[opposite]
        
        for i in range(len(views)//2):
            opposite = len(views)-1-i
            views[i], views[opposite] = views[opposite], views[i]
        return views