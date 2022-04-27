
import random

def generate():
    n = random.randrange(1, 20)
    d = {}
    for i in range(n - 1):
        d[i] = set()

    for i in range(n - 1):

        nodes = random.randrange(0, n - 1)
        
        for j in range(nodes):

            rand = random.randrange(0, n - 1)

            if j != rand and rand != i and i != j:
                d[i].add(rand)
                d[rand].add(i)

    print(n - 1)
    for i in d:
        print(i,end=" ")
        for j in d[i]:
            print(j,end=" ")
        
        print()


def main():
    generate()

if __name__ == "__main__":    
    main()