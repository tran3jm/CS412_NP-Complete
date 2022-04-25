import itertools
def main():
    n = int(input())
    g = {}
    vSet = []
    for _ in range(n):
        edges = input().split(" ")
        node = edges[0]
        vSet.append(node)
        g[node] = set()
        for x in range(1, len(edges)):
            g[node].add(edges[x])
    def exact():
        for x in range(1, len(vSet) + 1):
            combo = list(itertools.combinations(vSet, x))
            for item in combo:
                l = []
                for entry in list(item):
                    for v in g[entry]:
                        l.append(v)
                    l.append(entry)
                    if len(set(l)) == len(vSet): return list(item)
        return list(vSet)
    print(*exact())

if __name__ == "__main__":
    main()