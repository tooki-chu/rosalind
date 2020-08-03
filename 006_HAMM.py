'''
ROSALIND - Bioinformatics Stronghold
Problem: Counting Point Mutations
'''

def hamming(s,t):
    """
    Returns the Hamming distance between 2 strings of equal length
    """

    diff = 0

    for a,b in zip(s,t):
        if a!=b:
            diff += 1

    return diff


def main():
    with open('datasets/rosalind_hamm.txt', 'r') as f:
        s,t = f.read().strip().split("\n")

        print(hamming(s,t))

if __name__ == '__main__':
    main()