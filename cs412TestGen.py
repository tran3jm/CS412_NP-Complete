
import random

def generate():
    n = random.randrange(1, 20)
    d = {}
    for i in range(n):
        d[i] = set()

    for i in range(n):

        nodes = random.randrange(0, n)
        
        for j in range(nodes):

            rand = random.randrange(0, n)

            if j != rand and rand != i and i != j:
                d[i].add(rand)
                d[rand].add(i)

    print(n)
    for i in d:
        print(i,end=" ")
        for j in d[i]:
            print(j,end=" ")
        
        print()


def main():
    generate()

if __name__ == "__main__":    
    main()