from exactTesting import generate 
import sys, os

def main():
    x = int(input())
    for __ in range(5):
        findruntime(x)

def findruntime(x):
    f = open('file.txt', 'w')
    sys.stdout = f
    generate(x)
    sys.stdout.close()
    f.close()
    os.system('python3 exact.py < file.txt')

if __name__ == "__main__":
    main()