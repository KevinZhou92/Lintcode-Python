class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        from collections import deque
        
        indegrees = {}
        outdegrees = {}
        
        for prerequisite in prerequisites:
            pre_course = prerequisite[1]
            course = prerequisite[0]
            indegrees[course] = indegrees.get(course, 0) + 1
            outdegrees[pre_course] = outdegrees.get(pre_course, []) + [course]
            
        d = deque([])
        
        for i in range(numCourses):
            if i not in indegrees:
                d.append(i)
                
        res = []
        
        while d:
            course = d.popleft()
            res.append(course)
            if course in outdegrees:
                for course_num in outdegrees[course]:
                    indegrees[course_num] -= 1
                    if indegrees[course_num] == 0:
                        d.append(course_num)
                        
               
        return res if len(res) == numCourses else []