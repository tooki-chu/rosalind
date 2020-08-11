'''
ROSALIND - Bioinformatics Stronghold
Problem: Enumerating Gene Orders
'''

from itertools import permutations

def main():
    with open('datasets/rosalind_perm.txt', 'r') as f:
        n = int(f.read().strip())
        perm = list(permutations([x for x in range(1,n+1)]))
        
        print(len(perm))
        print('\n'.join (' '.join(str(j) for j in i) for i in perm))

        
if __name__ == '__main__':
    main()