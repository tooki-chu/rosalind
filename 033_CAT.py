'''
ROSALIND - Bioinformatics Stronghold
Problem: Catalan Numbers and RNA Secondary Structures
'''

from Bio import SeqIO

# global dictionary used for memoization
c = {}

def catalan(s):
    """
    Given an RNA string with the same number of occurrences of 
    'A' as 'U' and the same number of occurrences of 'C' as 'G'
    
    Return the total number of noncrossing perfect matchings of 
    basepair edges in the bonding graph of s
    """
    
    acgu = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    
    if len(s) == 0:
        return 1
    
    if s not in c:
        c[s] = sum([catalan(s[1:k]) * catalan(s[k+1:]) 
                    for k in range(1, len(s), 2) 
                    # if s[0] can pair with s[k]
                    if s[0] == acgu[s[k]]])
        
    return c[s]


def main():
    record = SeqIO.read('datasets/rosalind_cat.txt', 'fasta')
    s = str(record.seq)
    
    print(catalan(s) % 10**6)


if __name__ == '__main__':
    main()