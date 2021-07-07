'''
ROSALIND - Bioinformatics Stronghold
Problem: Counting Phylogenetic Ancestors
'''

def leaves(n):
    """
    Returns the number of internal nodes of any unrooted binary tree having n leaves
    """

    ans = n-2
    return(ans)


def main():
    with open('datasets/rosalind_inod.txt', 'r') as f:
        n = int(f.read())
        print(leaves(n))


if __name__ == '__main__':
    main()