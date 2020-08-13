'''
ROSALIND - Bioinformatics Stronghold
Problem: Enumerating k-mers Lexicographically
'''

from itertools import product


def main():
    with open("datasets/rosalind_lexf.txt", "r") as f:
        s,n = f.read().strip().split("\n")
        
        symbols = s.split()
        n = int(n)
        
        for indicies in product(range(len(symbols)), repeat=n):
            print("".join(list(symbols[i] for i in indicies)))


if __name__ == '__main__':
    main()