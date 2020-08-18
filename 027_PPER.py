'''
ROSALIND - Bioinformatics Stronghold
Problem: Partial Permutations
'''

from scipy.special import perm

def main():
    with open("datasets/rosalind_pper.txt", "r") as f:
        N, k = [int(x) for x in f.read().split()]
        print(int(perm(N, k)%1000000))


if __name__ == '__main__':
    main()