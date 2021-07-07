'''
ROSALIND - Bioinformatics Stronghold
Problem: Error Correction in Reads
'''

from Bio.Seq import Seq
from Bio import SeqIO

def rev_complement(s):
    """
    Returns the reverse complement of a given DNA string
    """

    rc = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

    return rc


def hamming(s,t):
    """
    Returns the Hamming distance between 2 strings of equal length
    """

    diff = 0

    for a,b in zip(s,t):
        if a!=b:
            diff += 1

    return diff


def corr_reads(seqs):
    """
    Given a collection of reads of equal length
    some of which have a single-nucleotide error
    
    Returns a list of all corrections 
    """
    
    # dictionary to store all seq counts
    seq_count = {}
    
    for s in seqs:
        
        if rev_complement(s) in seq_count:
            seq_count[rev_complement(s)] += 1
            
        elif s in seq_count:
            seq_count[s] += 1
            
        else:
            seq_count[s] = 1
            
    unique_corr_seqs = [k for k,v in seq_count.items() if v >= 2]
    all_corr_seqs = unique_corr_seqs + [rev_complement(u) for u in unique_corr_seqs]
    incorrect_seqs = set(seq_count.keys()) - set(unique_corr_seqs)
    
    for read1 in incorrect_seqs:
        
        correct = [read2 for read2 in all_corr_seqs if hamming(read1, read2) == 1]
                
        if len(correct) == 1:
            print(read1, "->", correct[0], sep="") 


def main():
    seqs = []
    for record in SeqIO.parse("datasets/rosalind_corr.txt", "fasta"):
        seqs.append(str(record.seq))
        
    corr_reads(seqs)



if __name__ == '__main__':
    main()