import sys
import random

def generate(num):
    counter = 0
    n = num
    d = {}
    for i in range(n):
        d[i] = set()

    for i in range(n):

        nodes = random.randrange(0, n)
        
        for _ in range(nodes):

            rand = random.randrange(0, n)

            if rand != i and rand not in d[i]:
                counter += 1
                d[i].add(rand)
                d[rand].add(i)

    print(n)
    for i in d:
        print(i,end=" ")
        for j in d[i]:
            print(j,end=" ")
        
        print()
    # print(counter)

def main():
    generate(int(sys.argv[1]))

if __name__ == "__main__":    
    main()