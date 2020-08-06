'''
ROSALIND - Bioinformatics Stronghold
Problem: Overlap Graphs
'''

from Bio import SeqIO

def overlaps(seqs, overlap=3):
    """
    Returns an adjacency list for a collection of 
    sequences in FASTA format
    
    overlap length is 3 by default
    """
    
    adj_list = []
    
    for s1 in seqs:
        for s2 in seqs:
            if s1.id != s2.id:
                if s1.seq[-overlap:] == s2.seq[:overlap]:
                    adj_list.append((s1.id, s2.id))
    
    return adj_list


def main():
    with open('datasets/rosalind_grph.txt', 'r') as f:
        records = list(SeqIO.parse(f, "fasta"))
        adj = overlaps(records)
        print("\n".join(" ".join(pair) for pair in adj))


if __name__ == '__main__':
    main()