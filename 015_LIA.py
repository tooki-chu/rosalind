'''
ROSALIND - Bioinformatics Stronghold
Problem: Independent Alleles
'''

from scipy.stats import binom

def main():
    with open('datasets/rosalind_grph.txt', 'r') as f:
        k,N = [int(i) for i in f.read().split()]
        genK = binom.sf(N-1, 2**k, .25, loc=0)
        print(round(genK, 3))


if __name__ == '__main__':
    main()