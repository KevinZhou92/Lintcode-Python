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



                    