'''
ROSALIND - Bioinformatics Stronghold
Problem: Computing GC Content
'''

from Bio import SeqIO
from Bio.SeqUtils import GC

def gc_content(sequences):
    """
    Returns the ID of the string with the highest GC-content
    follwed by the GC content of that string.
    """
    results = {}
    for record in sequences:
        results[record.id] = GC(record.seq)

    highest_record = max(results, key=results.get)
    highest_GC = results[highest_record]

    return highest_record, highest_GC


def main():
    with open('datasets/rosalind_gc.txt', 'r') as f:
        seqs = SeqIO.parse(f, "fasta")

        highest = gc_content(seqs)
        print(*highest)

if __name__ == '__main__':
    main()