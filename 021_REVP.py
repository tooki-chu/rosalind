'''
ROSALIND - Bioinformatics Stronghold
Problem: Locating Restriction Sites
'''

from Bio import SeqIO

def palindromes(sequence):
    """
    Returns a list of all the position and length 
    of every reverse palindrome in the DNA string
    having length between 4 and 12
    """
    
    S = sequence.seq
    
    # store (position, length) of every reverse palindrome
    P = []
    
    for i in range(len(S) + 1):
        # possible length of palindrome
        for j in range(4, 13):
            
            # make sure the slice is within the range of the sequence
            if i + j <= len(S):
                forward = S[i:i+j]
                reverse = forward.reverse_complement()
                
                # use the fact that reverse compliment of palindrome 
                # will be equal to the original subsequence
                if forward == reverse:
                    P.append((i+1, j))
    
    return P


def main():
    dna = SeqIO.read('datasets/rosalind_revp.txt', 'fasta')
    results = palindromes(dna)
    print('\n'.join (' '.join(str(y) for y in x) for x in results))


if __name__ == '__main__':
    main()