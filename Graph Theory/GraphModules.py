class Node:
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
        node = Node(node_name)
        self.nodelist.append(node)

    def add_random_nodes(self, length):
        asc = 65
        for iters in range (0, length):
            node = Node(chr(asc))
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