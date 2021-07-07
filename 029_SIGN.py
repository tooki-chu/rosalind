'''
ROSALIND - Bioinformatics Stronghold
Problem: Enumerating Oriented Gene Orderings
'''

from itertools import product

def SignedProb(N):
    """
    Returns a list of all signed permutations of length n 
    """
    
    permutations = []

    # find all signed permutations
    for indices in product(range(1, N+ 1), repeat = N):
        # to eliminate instances where the same index occurs more than once
        if len(set(indices)) == N:
            # VV IMPORTANT TRICK - all possible combination of +/- signs
            for combos in product([-1, 1], repeat=N):
                p = [integer * sign for integer, sign in zip(indices, combos)]
                permutations.append(p)
    
    return permutations


def main():
    with open("datasets/rosalind_sign.txt", "r") as f:
        n = int(f.read().strip())
        total = SignedProb(n)
        
        print(len(total))
        for i in range(len(total)):
            print(*total[i], sep=' ')


if __name__ == '__main__':
    main()