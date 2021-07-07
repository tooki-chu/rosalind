'''
ROSALIND - Bioinformatics Stronghold
Problem: Complementing a Strand of DNA
'''

def rev_complement(s):
    """
    Returns the reverse complement of a given DNA string
    """

    rc = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

    return rc


def main():
    with open('datasets/rosalind_revc.txt', 'r') as f:
        dna = f.read()

    print(rev_complement(dna))

if __name__ == '__main__':
    main()