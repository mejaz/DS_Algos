
from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        self.level = 0
        
class Edge(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        
    def insert_edge(self, node1, node2):
        n1 = None
        n2 = None
        for node in self.nodes:
            if node.value == node1:
                n1 = node
            if node.value == node2:
                n2 = node
        
        if not n1:
            n1 = Node(node1)
            self.nodes.append(n1)
        if not n2:
            n2 = Node(node2)
            self.nodes.append(n2)
            
        new_edge = Edge(n1, n2)
        
        n1.edges.append(new_edge)
        n2.edges.append(new_edge)
        self.edges.append(new_edge)

    def find_nodes_at_level(self, x):
        for node in self.nodes:
            node.visited = False
            node.level = 0
        start_node = self.nodes[1]
        self.bfs(start_node)
        
        count = 0
        for node in self.nodes:
            if node.level == int(x):
                count += 1
        
        return count
    
    def bfs(self, start_node):
        # print('start node is :', start_node.value)
        # final_list = []
        
        q = deque()
        start_node.level = 1
        start_node.visited = True
        q.append(start_node)
        
        while q:
            node = q.popleft()
            # print(node.value)
            # final_list.append(node.value)
            
            for e in node.edges:
                # print('node1 value : %s and visited : %s' % (e.node1.value, e.node1.visited))
                # print('node2 value : %s and visited : %s' % (e.node2.value, e.node2.visited))
                if e.node1.value == node.value and e.node2.visited == False:
                    # print(e.node2.value)
                    e.node2.visited = True
                    e.node2.level = node.level + 1
                    q.append(e.node2)

                if e.node2.value == node.value and e.node1.visited == False:
                    # print(e.node2.value)
                    e.node1.visited = True
                    e.node1.level = node.level + 1
                    q.append(e.node1)                    
                
        # return final_list


g = Graph()

n = int(input())

for _ in range(n-1):
    a, b = input().split()
    g.insert_edge(int(a), int(b))

x = input()
print(g.find_nodes_at_level(x))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
