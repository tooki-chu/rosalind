'''
ROSALIND - Bioinformatics Stronghold
Problem: Transitions and Transversions
'''

from Bio import SeqIO

def TransitionTransversionRatio(s1, s2):
    """
    Returns the transition/transversion ratio
    """
    
    l = len(s1)
    
    transition = 0
    transversion = 0

    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    
    for i in range(l):
        if s1[i] != s2[i]:
            # substituting a purine to another purine
            if s1[i] in purines and s2[i] in purines:
                transition += 1
            # substituting a pyrimadine to another pyrimidine
            elif s1[i] in pyrimidines and s2[i] in pyrimidines:
                transition += 1
            # substituting a purine to a pyrimidine or vice versa
            else:
                transversion += 1

    return transition / transversion


def main():
    records = list(SeqIO.parse("datasets/rosalind_tran.txt", "fasta"))
    s1 = str(records[0].seq)
    s2 = str(records[1].seq)
    
    ratio = TransitionTransversionRatio(s1, s2)
    
    print(round(ratio, 11))


if __name__ == '__main__':
    main()