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
        for u in range(n):
            if not visited[u]:
                for v in g[u]:
                    if not visited[v]:
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