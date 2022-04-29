import itertools
import time

def main():
    n = int(input()) # number of vertices in graph
    g = {} # graph
    vSet = [] # set of all vertices in graph
    edgeC = 0
    # setting up the graph and vertex set
    for _ in range(n):
        edges = input().split(" ")
        node = int(edges[0])
        vSet.append(node)
        g[node] = set()
        for x in range(1, len(edges)):
            g[node].add(int(edges[x]))
            edgeC += .5
    def exact():
        if edgeC == 0: return []
        # for every possible number of vertices
        for x in range(1, len(vSet) + 1):
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
        return []
    start_time = time.time()
    res = exact()
    if len(res) == 0: print("There are no edges.")
    else: 
        print("Min number:", len(res))
        print("Vertices:", *res)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()