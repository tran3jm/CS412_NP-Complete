
import random

def generate(num):
    counter = 0
    n = num
    d = {}
    for i in range(n):
        d[i] = set()

    for i in range(n):

        nodes = random.randrange(0, n)
        
        for j in range(nodes):

            rand = random.randrange(0, n)

            if j != rand and rand != i and i != j:
                counter += 1
                d[i].add(rand)
                d[rand].add(i)

    print(n)
    setCount = 1
    for i in d:
        if len(d[i]) == 0: print(i,end="")
        else: print(i,end=" ")
        for j in d[i]:
            if setCount == len(d[i]): print(j,end="")
            else: print(j,end=" ")
            setCount+=1
        setCount = 1
        print()
    # print(counter)

def main():
    generate()

if __name__ == "__main__":    
    main()