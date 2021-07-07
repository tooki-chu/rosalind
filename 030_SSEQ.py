'''
ROSALIND - Bioinformatics Stronghold
Problem: Finding a Spliced Motif
'''

from Bio import SeqIO
import re

def subseq(s, t):
    """
    Returns a list of indices of s in which the symbols 
    of t appear as a subsequence of s 
    """
    
    indicies = []
    x = 0 # pointer

    for char in t:
        # re.compile(pattern).search(string, start pos)
        match = re.compile(char).search(s, x) 

        if match is not None:
            indicies.append(match.start() + 1)
            x = match.start() + 1

    return indicies


def main():
    records = list(SeqIO.parse("datasets/rosalind_sseq.txt", "fasta"))
    s = str(records[0].seq)
    t = str(records[1].seq)
    indx = subseq(s, t)
    
    print(*indx, sep=' ')


if __name__ == '__main__':
    main()