'''
ROSALIND - Bioinformatics Stronghold
Problem: Mendel's First Law
'''

def mendel(k,m,n):
    """
    Returns the probability that two randomly selected mating organisms 
    will produce an individual that displays the dominant phenotype.
    k - homozygous dominant individuals 
    m - heterozygous individuals
    n - homozygous recessive individuals
    """

    # total population
    N = int(k + m + n)

    # P(homozygous recessive)
    hh = (m*n + 0.25*m*(m-1) + n*(n-1) ) / (N*(N-1))

    # P(possess at least 1 dominant phenotype)
    return (1-hh)


def main():
    with open('datasets/rosalind_iprb.txt', 'r') as f:
        (k,m,n) = (int(val) for val in f.readline().split())

        print(mendel(k,m,n))

if __name__ == '__main__':
    main()