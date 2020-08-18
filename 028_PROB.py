'''
ROSALIND - Bioinformatics Stronghold
Problem: Introduction to Random Strings
'''

from math import log10

def CGprobability(seq, A):
    """
    Given a string S and an array A
    Return an array B having the same length as A in which B[k] 
    represents the common logarithm of the probability that a random 
    string constructed with the GC-content found in A[k] will match s exactly
    """
    
    # count the number of A/T and G/C in s
    ATs = s.count("A") + s.count("T")
    GCs = s.count("G") + s.count("C")
    
    # probability = (freq of G/C)^(number of GCs) * (freq of A/T)^(number of ATs)
                # = log((freq of G/C)^(number of GCs)) + log((freq of A/T)^(number of ATs))
                # = (number of GCs) * log(freq of G/C) + (number of ATs) * log(freq of A/T)
            
    # freq of G/C = x/2
    # freq of A/T = (1-x)/2
    B = [round( GCs * log10(x/2) + ATs * log10((1-x) / 2), 3 )for x in A]
    
    return B


def main():
    with open("datasets/rosalind_prob.txt", "r") as f:
        s = f.readline().strip('\n')
        A = [float(x) for x in f.readline().split()]
        
        print(CGprobability(s, A))


if __name__ == '__main__':
    main()