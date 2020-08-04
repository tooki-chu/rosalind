'''
ROSALIND - Bioinformatics Stronghold
Problem: Translating RNA into Protein
'''

from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

def translate(s):
    """
    Returns the protein string encoded by mRNA string
    """

    mRNA = Seq(s, generic_rna)
    prot = mRNA.translate(to_stop = True)

    return prot


def main():
    with open('datasets/rosalind_prot.txt', 'r') as f:
        prot = translate(f.read())
        print(prot)

if __name__ == '__main__':
    main()