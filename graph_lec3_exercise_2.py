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


def edge_validation(src, dest):
    src_node = [char for char in str(src)]
    dest_node = [char for char in str(dest)]
    permutation_len = len(src_node)
    chars_allowed_to_permute = 2
    target_permute_param = permutation_len - chars_allowed_to_permute
    permute_allowed = 0
    try:
        for char in range(permutation_len):
            if src_node[char] != dest_node[char]:
                if src_node[char] == dest_node[char + 1] \
                        and src_node[char + 1] == dest_node[char]:
                    permute_allowed += 1
    except IndexError:
        pass

    return permute_allowed == target_permute_param


for node in range(len(nodes)):
    for next_node in range(node + 1, len(nodes)):
        if edge_validation(nodes[node], nodes[next_node]):
            g.addEdge(Edge(nodes[node], nodes[next_node]))

print(g)
