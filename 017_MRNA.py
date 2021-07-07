'''
ROSALIND - Bioinformatics Stronghold
Problem: Inferring mRNA from Protein
'''

def mrna(prot):
    """
    Returns the total number of different RNA strings from which
    the given protein string could have been translated
    modulo 1 000 000
    """
    
    # number of ways each AA can be encoded
    freq_table = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    '*': 3
    }
    
    # given protein string does not have STOP at the end
    # but need to account for 3 different stop codons
    total = 3
    
    for aa in prot:
        total *= freq_table[aa] % 1000000
        
    return total % 1000000


def main():
    with open('datasets/rosalind_mrna.txt', 'r') as f:
        protein = f.read().strip()
        total = mrna(protein)
        print(total)


if __name__ == '__main__':
    main()