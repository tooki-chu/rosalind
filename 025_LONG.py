'''
ROSALIND - Bioinformatics Stronghold
Problem: Genome Assembly as Shortest Superstring
'''

import copy
from Bio import SeqIO

def superstring(seqs):
    """
    Given that there exists a unique way to assemble a superstring
    from these reads by gluing together pairs of reads that overlap 
    by more than half their length
    
    Return a shortest superstring containing all the given strings
    """
    
    n = len(seqs)
    
    overlaps = [] # store tuples of overlap pairs 
    start = [i for i in range(n)] # determine the leftmost read
    for i in range(n):
        for j in range(n):
            if i != j:
                # since reads should overlap by more than half their length
                half = len(seqs[j]) // 2
                # see if the first half of read j is within read i 
                if seqs[j][:half] in seqs[i]:
                    overlaps.append((i, j))
                    start.remove(j)
    
    # starting with the leftmost string
    prv_index = start[0]
    sprstring = seqs[prv_index]
    
    # piece together unique fragments from each read
    for i in range(n-1): 
        
        # index of read that overlaps with the last one
        nxt_index = [pair[1] for pair in overlaps if pair[0] == prv_index]
        # full length of next read
        nxt = seqs[nxt_index[0]]
        
        # for next iteration
        prv_index = nxt_index[0]
        
        # determine exact length of overlap
        half = len(nxt)//2
        for k in range(half, len(nxt)):
            if nxt[:k] not in sprstring:
                break
                
        # append non-overlapping slice
        sprstring += nxt[k-1:]
    
    return sprstring


def main():
    reads = []
    for record in SeqIO.parse("datasets/rosalind_long.txt", "fasta"):
        reads.append(str(record.seq))
        
    sprstr = superstring(reads)
    
    print(sprstr)


if __name__ == '__main__':
    main()