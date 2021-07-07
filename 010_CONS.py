'''
ROSALIND - Bioinformatics Stronghold
Problem: Consensus and Profile
'''

import numpy as np
from collections import Counter
from Bio import SeqIO

def ACGTprofile(seqs):
    """
    Returns a 4 x n matrix reprsenting the frequency of a 
    nucleotide at each position for a collection of strings
    of the same length n
    """
    
    # length of each string
    n = len(seqs[0])
    
    # empty matrix
    matrixP = np.zeros(shape=(4, n), dtype=int)
    
    # count frequency of 'A','C','G','T' at each position
    ACGTcounts = map(Counter, zip(*seqs))
    
    j = 0
    # at each position along the string
    for position in ACGTcounts:
        # record counts for 'A','C','G','T'
        matrixP[:, j] = np.array([position[nt] for nt in "ACGT"])
        # move along to next position
        j += 1

    return matrixP


def consensus(seqs):
    """
    Returns a consensus string of length n formed by 
    taking the most common symbol at each position
    """
    
    # count frequency of 'A','C','G','T' at each position
    ACGTcounts = map(Counter, zip(*seqs))
    
    # choose the most frequent of the 4 bases at each position
    consensus_seq = "".join(position.most_common(1)[0][0] for position in ACGTcounts)
    
    return consensus_seq


def main():
    with open('datasets/rosalind_cons.txt', 'r') as f:
        records = SeqIO.parse(f, "fasta")
        seqs = [str(record.seq) for record in records]
        
    # consensus sequence
    print(consensus(seqs))
        
    # profile matrix
    profile = ACGTprofile(seqs)
    
    # print in required format
    for j, nt in zip(range(4),"ACGT"):
        print(nt + ": " + " ".join(str(i) for i in profile[j]))


if __name__ == '__main__':
    main()