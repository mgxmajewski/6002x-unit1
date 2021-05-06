# Good approach - try to make it work
# author: Richard_B_UK
from handout_graph import Node, Graph, Edge

nodes = [Node("ABC"),
         Node("ACB"),
         Node("BAC"),
         Node("BCA"),
         Node("CAB"),
         Node("CBA")]

g = Graph()

for n in nodes:
    g.addNode(n)


def addAllEdges(nodes):
    """Assumes all nodes have the same length"""
    temp = nodes[:]
    print(len(temp))
    while len(temp) > 1:
        current = temp.pop(0)
        for node in temp:
            diffs = ""
            for i in range(len(node)):
                diffs += str(current[i] == node[i])
            if diffs.count("False") == 2 and diffs.count("FalseFalse") == 1:
                g.addEdge(Edge(current, node))


print(addAllEdges(nodes))
