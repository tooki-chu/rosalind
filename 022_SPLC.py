'''
ROSALIND - Bioinformatics Stronghold
Problem: RNA Splicing
'''

from Bio import SeqIO
import re

def splice(S, intron_list):
    """
    Given a string S and a list of substrings that are introns
    in fasta format
    Returns string S with all introns removed
    """
    
    exons = str(S.seq)
    
    for record in intron_list:
        
        intron = str(record.seq)
        
        match = re.search(intron, exons)
        
        update = exons[:match.start()] + exons[match.end():]
        
        exons = update
    
    return exons


def main():
    dna = next(SeqIO.parse('datasets/rosalind_splc.txt', 'fasta'))
    introns = SeqIO.parse('datasets/rosalind_splc.txt', 'fasta')
    
    exons = splice(dna, introns)
    codons = Seq(exons, generic_dna)
    protein = codons.translate(to_stop=True)
    
    print(protein)


if __name__ == '__main__':
    main()