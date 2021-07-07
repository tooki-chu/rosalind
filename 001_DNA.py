'''
ROSALIND - Bioinformatics Stronghold
Problem: Counting DNA Nucleotides
'''

def count_nt(s):
    """
    Returns a list of the number of occurrences of 
    'A', 'C', 'G', and 'T' in string s
    """

    counts = [s.count(nt) for nt in 'ACGT']

    return counts

def main():
    with open('datasets/rosalind_dna.txt', 'r') as f:
        dna = f.read()

    # print the counts
    print(*count_nt(dna))

if __name__ == '__main__':
    main()