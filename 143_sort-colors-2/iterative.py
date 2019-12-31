'''
=> Iteration
Iterative O(k / 2)times, every iteration remove the current min and max color
Time: O(nk)
Space: O(1)
'''
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors:
            return 
        
        count = 0
        start, end = 0, len(colors) - 1
        min_color = 1
        max_color = k
        while count < k:
            index = start
            while index <= end:
                if colors[index] == min_color:
                    colors[start], colors[index] = colors[index], colors[start]
                    start += 1
                    index += 1
                elif colors[index] == max_color:
                    colors[end], colors[index] = colors[index], colors[end]
                    end -= 1
                else:
                    index += 1
                    
            min_color += 1
            max_color -= 1
            count += 2
            
        return