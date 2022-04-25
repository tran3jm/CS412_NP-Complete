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
                l = set()
                for entry in list(item):
                    for v in g[entry]:
                        l.add(v)
                    l.add(entry)
                if len(l) == len(vSet): return list(item)
    print(*exact())

if __name__ == "__main__":
    main()