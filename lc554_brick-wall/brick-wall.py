class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0
        
        rows = len(wall)
        length = sum(wall[0])
        
        edges = {}
        for row in wall:
            edge = 0
            for index in range(len(row) - 1):
                edge += row[index]
                edges[edge] = edges.get(edge, 0) + 1
        
        res = rows
        for edge in sorted(edges.keys()):
            res = min(res, rows - edges[edge])
                
        return res
        