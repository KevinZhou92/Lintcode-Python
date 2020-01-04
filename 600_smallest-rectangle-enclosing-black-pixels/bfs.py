'''
Time: O(row * col)
Space: O(row * col)
'''
from collections import deque
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        up, down, left, right = sys.maxsize, -sys.maxsize-1, sys.maxsize, -sys.maxsize - 1,
        
        rows = len(image)
        cols = len(image[0])
        queue = deque([])
        queue.append((x, y))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        image[x][y] = '0'
        while queue:
            node_x, node_y = queue.popleft()
            up = min(up, node_x)
            down = max(down, node_x)
            left = min(left, node_y)
            right = max(right, node_y)
            for i in range(4):
                new_x, new_y = node_x + dx[i], node_y + dy[i]
                if 0 <= new_x < rows and 0 <= new_y < cols and image[new_x][new_y] == '1':
                    queue.append((new_x, new_y))
                    image[new_x][new_y] = '0'
            print(len(queue))
        return (down - up + 1) * (right - left + 1)