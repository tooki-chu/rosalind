'''
ROSALIND - Bioinformatics Stronghold
Problem: k-Mer Composition
'''

from Bio import SeqIO
from itertools import product

def kmer_composition(dna, k=4):
    """
    Returns a list consisting of frequencies of all possible 
    4-mer composition of DNA string s, ordered alphabetically 
    """
    
    # all possible 4-mer compositions of ACTG
    kmers = [''.join(i) for i in product('ACGT', repeat=k)]
    
    # dict to store count of each 4-mer
    kmer_counts = dict.fromkeys(kmers, 0)
    
    # iterate through string s in blocks of 4
    # len(s) - k + 1 ways to have slices of length k
    for i in range(len(dna) - k + 1):
        block = dna[i:i+k]
        kmer_counts[block] += 1
        
    values = [v for k,v in sorted(kmer_counts.items())]

    return values


def main():
    s = str(SeqIO.read('datasets/rosalind_kmer.txt', 'fasta').seq)
    v = kmer_composition(s)
    print(*v, sep=" ")


if __name__ == '__main__':
    main()