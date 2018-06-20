class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        
class Edge(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.weight = 0
        

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.nodes_wts_list = []
        self.final_sorted_edges = []
        self.mst = []
        
    def insert_edge(self, node1, node2, weight):
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
        new_edge.weight = weight
        
        n1.edges.append(new_edge)
        n2.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_nodes_wts_tuple_from_adjmtx(self, adjmatx):
    	''' extract tuples in the form of node1, node2 and weight '''

    	for v, edges in adjmatx.items():
    		for e in edges:
    			if v < e[0]:
    				self.nodes_wts_list.append((v, e[0], e[1]))

    	return self.nodes_wts_list

    def remove_high_weight_btw_same_nodes(self):

		edge_dict = {}

		for edge in self.edges:
			# key = '%s%s' % (edge.node1.value, edge.node2.value)
			if not edge_dict.get(edge):
				edge_dict[edge] = edge.weight
			else:
				if edge_dict[edge] > edge.weight:
					edge_dict[edge] = edge.weight

		self.final_sorted_edges = edge_dict.items()
		self.final_sorted_edges.sort(key=lambda x: x[0].weight)
		return self.final_sorted_edges


    def create_mst(self):
        for edge in self.final_sorted_edges:
        	if self.mst:
        		self.mst.append(edge)
        	else:
        		pass




adj = graph1 = {
    'A': [('B', 3), ('C', 5), ('D', 3), ('A', 10), ('B', 1)],
    'B': [('A', 3), ('A', 1), ('C', 4), ('D', 2)],
    'C': [('B', 4), ('D', 1)],
    'D': [('A', 3), ('B', 2), ('C', 1)],
}

g = Graph()
n_list = g.get_nodes_wts_tuple_from_adjmtx(adj)

for edge in n_list:
	g.insert_edge(*edge)
print g.remove_high_weight_btw_same_nodes()
