class Solution:
    """
    @param wall: a list of rows
    @return: the number of crossed bricks
    """
    def leastBricks(self, wall):
        # write your code here
        row_count = len(wall)
        edge_count = {}
        for row in wall:
            edge = 0
            for i in range(len(row) - 1):
                edge += row[i]
                edge_count[edge] = edge_count.get(edge, 0) + 1
            
        res = row_count
        for edge in edge_count:
            res = min(res, row_count - edge_count[edge])
            
        return res