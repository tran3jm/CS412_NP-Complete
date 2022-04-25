def main():
    n = int(input())
    g = {}
    for _ in range(n):
        edges = input().split(" ")
        node = edges[0]
        g[node] = set()
        for x in range(1, len(edges)):
            g[node].add(edges[x])

if __name__ == "__main__":
    main()