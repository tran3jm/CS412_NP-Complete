import itertools
def main():
    n = int(input()) # number of vertices in graph
    g = {} # graph
    vSet = [] # set of all vertices in graph
    # setting up the graph and vertex set
    for _ in range(n):
        edges = input().split(" ")
        node = edges[0]
        vSet.append(node)
        g[node] = set()
        for x in range(1, len(edges)):
            g[node].add(edges[x])
    def exact():
        # for every possible number of vertices
        for x in range(1, len(vSet)):
            # generate combinations
            combos = list(itertools.combinations(vSet, x))
            # for every combination
            for item in combos:
                l = []
                # get the vertices connected to each resulting vertex
                # and add them to l
                for entry in list(item):
                    for v in g[entry]:
                        l.append(v)
                    l.append(entry)
                    # if all vertices are included in l
                    # return this specific combination
                    if len(set(l)) == len(vSet): return list(item)
        return list(vSet)
    print(*exact())

if __name__ == "__main__":
    main()
 
