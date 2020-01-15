'''
=> Topological Sort
Time: O(V + E)

Note:
Please be careful on defaultdict, make sure if it is list or set you want to use.
Remember that there will be duplicates in the input

Always iterate given input, instead of a structure that could change its size, for example, a dict.

'''
from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if not prerequisites or not numCourses:
            return True
        
        indegrees, outdegrees = defaultdict(int), defaultdict(list)
        for prerequisite in prerequisites:
            indegrees[prerequisite[0]] += 1
            outdegrees[prerequisite[1]].append(prerequisite[0])
        
        queue = deque([course for course in range(numCourses) if course not in indegrees])
        res = []
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in outdegrees[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(res) == numCourses