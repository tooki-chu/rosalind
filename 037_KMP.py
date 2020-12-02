'''
ROSALIND - Bioinformatics Stronghold
Problem: Speeding Up Motif Finding
'''

from Bio import SeqIO

def FailureArray(s):
    """
    Returns failure array of s
    """
    n = len(s)

    j = 0 # current longest matching streak 
    failure = [0] * n

    for i in range(1, n):
        while j>0 and s[i] != s[j]:
            # retrace your step to the last point where all char to the left are matched
            j = failure[j-1]

        if s[i] == s[j]:
            j += 1
            # store index of element to the right of match
            failure[i] = j

        elif s[i] != s[j] and j==0: # maybe could do elif s[i] = s[0]: failure[i] = 0
            failure[i] = j

    return failure


def main():
    s = str(SeqIO.read('datasets/rosalind_kmp.txt', 'fasta').seq)
    f = FailureArray(s)
    print(*f, sep=" ")


if __name__ == '__main__':
    main()