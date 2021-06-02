def de_Bruijn(sequence, k):
    edges = []
    nodes = set()
    eulerian_walk = ''
    for i in range(len(sequence) - k + 1):
        eulerian_walk = eulerian_walk + sequence[i:i+k-1] + '->'
        edges.append((sequence[i:i+k-1], sequence[i+1:i+k]))
        nodes.add(sequence[i:i+k-1])
        nodes.add(sequence[i+1:i+k])
    eulerian_walk = eulerian_walk[:-2]
    #print(eulerian_walk)
    return nodes, edges, eulerian_walk

def main():
    L = "GACTTACGTACT"
    k = 3
    nodes, edges, eulerian_walk = de_Bruijn("GACTTACGTACT", 3)
    print("nodes: ",nodes)  #total nodes in de Bruijn Graph.
    #print("edges: ",edges) #edges from one nodes to another node.
    print("Eulerian walk: ",eulerian_walk)

main()

