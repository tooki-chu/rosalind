'''
ROSALIND - Bioinformatics Stronghold
Problem: Rabbits and Recurrence Relations 
'''

def fibonacci(n,k):
    """
    Returns the total number of rabbit pairs after n months.
    Given that we begin with 1 pair of rabbits and each pair
    of reproduction-age rabbits produces a litter of k rabbit pairs.
    """

    # base case
    # applies to first 2 months
    if n < 2:
        return(n)
    
    # any given month thereafter
    else:
        # rabbits alive in previous month
        gen1 = fibonacci(n-1, k)
        # number of matings = rabbits alive 2 months prior
        gen2 = fibonacci(n-2, k)
        # total number of rabbits = previous gen + offspring
        return(gen1 + (gen2 * k))


def main():
    with open('datasets/rosalind_fib.txt', 'r') as f:
        n, k = [int(i) for i in f.read().strip().split(' ')]

    print(fibonacci(n,k))

if __name__ == '__main__':
    main()