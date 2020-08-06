'''
ROSALIND - Bioinformatics Stronghold
Problem: Mortal Fibonacci Rabbits
'''

def rabbits(n, m):
    """
    Returns total number of pairs of rabbits after n months
    assuming that all rabbits die after m months
    and rabbits produce 1 pair of offspring each time
    """
    
    # empty array of length m to keep track of rabbits at each age group
    ages = [0] * m
    
    # start with 1 pair of rabbits
    ages[-1] = 1
    
    # for the following n months
    for i in range(1, n):
        # count new offspring produced by all adult rabbits
        new_rabbits = sum(ages[:-1])
        # rabbits get older - shift to left
        ages[:-1] = ages[1:]
        # record new offspring only after updating all age groups
        ages[-1] = new_rabbits

    return sum(ages)


def main():
    with open('datasets/rosalind_fibd.txt', 'r') as f:
        n, m = [int(i) for i in f.readline().split()]
        print(rabbits(n, m))


if __name__ == '__main__':
    main()