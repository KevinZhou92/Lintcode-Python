class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        
        numbers.sort()
        res = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            l, r = i + 1, len(numbers) - 1
            while l < r:
                sums = numbers[l] + numbers[r]
                if sums + numbers[i] == 0:
                    res.append([numbers[i], numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r + 1]:
                        r -= 1
                elif sums + numbers[i] < 0:
                    l += 1
                else:
                    r -= 1
            
            
        return res