'''
ROSALIND - Bioinformatics Stronghold
Problem: Finding a Shared Spliced Motif
'''

from Bio import SeqIO
import numpy as np

def LCS_lookup(x, y, m, n):
    """
    Returns filled lookup table
    """
    T = np.zeros((m+1, n+1), dtype=int)
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i][j-1], T[i-1][j])

    return T


def LCS(x, y, m, n, T):
    """
    Backtracks from bottom right to top left of lookup table to read LCS
    """
    # return empty string if we have reached the end of either sequence
    if m == 0 or n == 0:
        return str()

    # if last character of X and Y matches
    if x[m - 1] == y[n - 1]:
        # append current character (X[m-1] or Y[n-1]) to LCS of
        # substring X[0..m-2] and Y[0..n-2]
        return LCS(x, y, m - 1, n - 1, T) + x[m - 1]

    # if the last character of X and Y are different

    # if top cell of current cell has more value than the left
    # cell in lookup table, then drop current character of X and find LCS
    # of substring X[0..m-2], Y[0..n-1]
    if T[m - 1][n] > T[m][n - 1]:
        return LCS(x, y, m - 1, n, T)
    
    else:
        # if left cell of current cell has more value than the top
        # cell, then drop current character of Y and find LCS
        # of substring X[0..m-1], Y[0..n-2]
        return LCS(x, y, m, n - 1, T)


def main():
    records = list(SeqIO.parse("datasets/rosalind_lcsq.txt", "fasta"))

    x = str(records[0].seq)
    y = str(records[1].seq)

    m = len(x)
    n = len(y)
    
    matrix = LCS_lookup(x, y, m, n)
    print(LCS(x, y, m, n, matrix))
    

if __name__ == '__main__':
    main()