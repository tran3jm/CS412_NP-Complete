"""
The code takes n vertices with their associated edges. It then generates every possible combination
of vertices, starting with groups of 2 and working up to groups of n-1. It then checks each individual
combination to determine if it's the min cover. It does this by storing every edge associated with
each vertex in the combination (without storing the same edge twice), 
then compares the size of that set to the total number of edges. If it's equal, that particular 
combination is returned as the min covering. 
If there are no edges in the graph, it prints "There are no edges."
"""
import itertools
def main():
    n = int(input()) # number of vertices in graph
    g = {} # graph
    vSet = [] # set of all vertices in graph
    edgeC = 0 # number of edges
    # setting up the graph and vertex set
    for _ in range(n):
        edges = input().split(" ")
        node = int(edges[0])
        vSet.append(node)
        g[node] = set() # every vertex corresponds to a set of edges
        for x in range(1, len(edges)):
            g[node].add(int(edges[x])) # add edge
            edgeC += .5 # don't count the same edge twice
    def exact():
        if edgeC == 0: return [] # no edges
        # for every possible number of vertices 1 through n-1
        for x in range(1, len(vSet)):
            # generate combinations
            combos = list(itertools.combinations(vSet, x))
            # for every combination
            for combo in combos:
                edgeSet = set()
                # for every entry in combination
                for entry in list(combo):
                    # for every vertex in the entry
                    for v in g[entry]:
                        # add its edges to edgeSet
                        if (v, entry) not in edgeSet: edgeSet.add((entry, v))
                    # return when length of edgeSet = # of edges
                    if len(edgeSet) == edgeC: return list(combo)
        return list(edgeSet) # all vertices required for solution, shouldn't ever get to this line
    res = exact()
    if len(res) == 0: print("There are no edges.")
    else:
        print("Min number:", len(res)) # this number should always at most be n-1
        print("Vertices:", *res)

if __name__ == "__main__":
    main()
"""
Worst case: fully connected graph
Best case: no edges
"""