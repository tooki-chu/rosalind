'''
ROSALIND - Bioinformatics Stronghold
Problem: Finding a Shared Motif
'''

from Bio import SeqIO

def LCSub(fasta_records):
    """
    Returns a longest common substring of a collection of DNA strings
    """
    
    seqs = [str(record.seq) for record in fasta_records]
    
    # total number of sequences
    N = len(seqs)
    
    # use first seq as reference
    ref = seqs[0]
    l = len(ref)
    
    # store longest common sequence
    lcs = ""
    
    for i in range(l):
        for j in reversed(range(i+1, l+1)):
            stem = ref[i:j]
            
            # start with count of 1 as reference string contains stem
            count = 1
            
            # scan through all other strings for the stem
            for k in seqs[1:]:
                if stem in k:
                    count += 1
                else:
                    break
                    
            # if all DNA strings contain this stem 
            # and this is currently the longest stem
            if count == N and len(lcs) < len(stem):
                lcs = stem
    
    return lcs


def main():
    with open('datasets/rosalind_grph.txt', 'r') as f:
        records = list(SeqIO.parse(f, "fasta"))
        print(LCSub(records))


if __name__ == '__main__':
    main()