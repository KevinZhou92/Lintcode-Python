'''
=> Modified Quick Sort
Notice the special modification we have on line 29, we want a strict distribution that all the color that is smaller than or equal to pivot will appear on left, otherwise right.
This way we will not have dead loop
Time: O(nlogk)
Space: O(logk)
'''
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.quick_sort(colors, 0, len(colors) - 1, 1, k)
        
    def quick_sort(self, colors, start, end, colorFrom, colorTo):
        if colorFrom >= colorTo:
            return
        
        if start >= end:
            return
        
        pivot = colorFrom + (colorTo - colorFrom) // 2
        
        l, r = start, end
        while l <= r:
            while l <= r and colors[l] <= pivot:
                l += 1
            while l <= r and colors[r] > pivot:
                r -= 1
            
            if l <= r:
                colors[l], colors[r] = colors[r], colors[l]
                l += 1
                r -= 1
                
        self.quick_sort(colors, start, r, colorFrom, pivot)
        self.quick_sort(colors, l, end, pivot + 1, colorTo)


'''
=> Iteration
Iterative O(k / 2)times, every iteration remove the current min and max color
Time: O(nk)
Space: O(1)
'''
class Solution2:
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
                    