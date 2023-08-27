from pandas import DataFrame
class _Node:
    def __init__(self, name) -> None:
        self.edges = []
        self.name = name
    def __repr__(self) -> str:
        return f"{self.name}"
    

class UndirectedGraph:
    def __init__(self) -> None:
        self.nodelist = []
        self.connections = {}

    def add_node(self, node_name):
        for nodeIndex in range (0, len(self.nodelist)):
            if self.nodelist[nodeIndex].name == node_name:
                raise Exception('Node already exists. Try Again')
        node = _Node(node_name)
        self.nodelist.append(node)

    def add_random_nodes(self, length):
        asc = 65
        for iters in range (0, length):
            node = _Node(chr(asc))
            self.nodelist.append(node)
            asc+=1

    def add_edge(self, fro, to):
        count_to = 0
        count_fro = 0
        for nodeIndex in range (0, len(self.nodelist)):
            if self.nodelist[nodeIndex].name == fro:
                count_fro+=1
            elif self.nodelist[nodeIndex].name == to:
                count_to+=1

        if count_to == 0 or count_fro == 0:
            raise Exception('Node not a part of defined graph. Try a different node or define it then try again.')
        
        if fro not in self.connections:
            self.connections[fro] = [to]
        else:
            self.connections[fro].append(to)

        if to not in self.connections:
            self.connections[to] = [fro]
        else:
            self.connections[to].append(fro)

    def remove_edge(self, fro, to):
        if fro not in self.connections[to] or to not in self.connections[fro]:
            raise Exception('Edges are not connected')
        else:
            self.connections[to].remove(fro)
            self.connections[fro].remove(to)
        
    def display(self):
        return self.connections
    
    def construct_adjacency_matrix(self):
        adj_mat = []
        adj_mat_df = DataFrame(index=[nodes for nodes in self.connections], columns=[nodes for nodes in self.connections])
        for rows in adj_mat_df.index:
            for cols in self.connections[rows]:
                adj_mat_df[rows][cols] = 1
        adj_mat_df.fillna(0, inplace=True)
        for rows in adj_mat_df.index:
            row = []
            for cols in adj_mat_df.columns:
               row.append(adj_mat_df[cols][rows])
            adj_mat.append(row)

        return adj_mat
          