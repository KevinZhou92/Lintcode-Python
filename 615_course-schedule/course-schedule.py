'''
=> DFS
Time: O(n^2)
'''
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        indegrees = {}
        outdegrees = {}
        prerequisites = [(prerequisite[0], prerequisite[1]) for prerequisite in prerequisites]
        
        for prerequisite in set(prerequisites):
            pre_course = prerequisite[0]
            course = prerequisite[1]
            indegrees[course] = indegrees.get(course, 0) + 1
            outdegrees[pre_course] = outdegrees.get(pre_course, []) + [course]
        
        for i in range(numCourses):
            if self.dfs(i, indegrees, outdegrees, set()):
                return False
                
        return True
        
    # check if there is a cycle
    def dfs(self, course_num, indegrees, outdegrees, visited):
        visited.add(course_num)
        
        if course_num in outdegrees:
            for course in outdegrees[course_num]:
                if course in visited:
                    return True
                if self.dfs(course, indegrees, outdegrees, visited):
                    return True

        visited.remove(course_num)
        
        return False

'''
=> Topological Sort
Time: O(V + E)
'''
class Solution2:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        from collections import deque
        # write your code here
        indegrees = {}
        outdegrees = {}
        
        for prerequisite in prerequisites:
            pre_course = prerequisite[0]
            course = prerequisite[1]
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
                for next_course in outdegrees[course]:
                    indegrees[next_course] -= 1
                    if indegrees[next_course] == 0:
                        d.append(next_course)
                        
        return numCourses == len(res)