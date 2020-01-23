'''
=> Union Find

Note: In union find, after several connect operations, we will still have a unbalanced tree and the path is 
not compressed completely. We need to do find on each node to let them point to real father

'''
class UnionFind:
    def __init__(self, total):
        self.count = total
        self.fathers = {}
        self.children = {}
        
    def find(self, index):
        path = []
        while index != self.fathers[index]:
            path.append(index)
            index = self.fathers[index]
        
        if index not in self.children:
            self.children[index] = set([index])
        
        for p in path:
            self.children[index].add(p)
            self.fathers[p] = index
            
        return index
        
    def connect(self, index1, index2):
        fathers1 = self.find(index1)
        fathers2 = self.find(index2)
        
        if fathers1 != fathers2:
            self.fathers[fathers1] = fathers2
            self.find(index1)
            self.find(index2)
        
class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return  []
            
        uf = UnionFind(len(nodes))
        for node in nodes:
             uf.fathers[node.label] = node.label
        
        for node in nodes:
            for neighbor in node.neighbors:
                uf.connect(node.label, neighbor.label)
        
        visited = set()
        res = []
        for node in nodes:
            father = uf.find(node.label)
            
        for node in nodes:
            father = uf.find(node.label)
            if father not in visited:
                visited.add(father)
                res.append(sorted(list(uf.children[father])))
        
        
                
        return res
        