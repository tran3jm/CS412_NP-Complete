def main():
    n = int(input()) # number of vertices in graph
    g = {} # graph
    vSet = [] # set of all vertices in graph
    for _ in range(n):
        edges = [int(x) for x in input().split()]
        node = edges[0]
        vSet.append(node)
        g[node] = set()
        for x in range(1, len(edges)):
            g[node].add(edges[x])
    def approx():
        visited = [False] * n
        # find next edge
        for u in range(n):
            # u must not be visited
            if not visited[u]:
                # v is a vertex connected to u and must not be visited
                for v in g[u]:
                    if not visited[v]:
                        # if a u and v have been found and have not been visited then
                        # we've found a new edge and we can add both to the visited list
                        visited[u] = True
                        visited[v] = True
                        break
        result = []
        for vertex in range(len(visited)):
            if visited[vertex]:
                result.append(vertex)
        return result
    res = approx()
    if len(res) == 0: print("There are no edges.")
    else: print(*res)

if __name__ == "__main__":
    main()