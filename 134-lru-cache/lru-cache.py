class Node:
    def __init__(self, k,v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        
class LRUCache:
    def __init__(self, capacity):
        # do intialization if necessary
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.node_map = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.node_map.keys():
            node = self.node_map[key]
            self._remove(node)
            self._add(node)
            return node.val
            
        return -1
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.node_map:
            node = self.node_map[key]
            self._remove(node)
        
        node = Node(key, value)
        self.node_map[key] = node
        self._add(node)
        
        if self.capacity < len(self.node_map.keys()):
            self.node_map.pop(self.head.next.key)
            self._remove(self.head.next)
        
        
    def _remove(self, node):
        pre_node = node.prev
        next_node = node.next
        pre_node.next = next_node
        next_node.prev = pre_node
    
    def _add(self, node):
        cur_tail = self.tail.prev
        cur_tail.next = node
        node.prev = cur_tail
        node.next = self.tail
        self.tail.prev = node   
        