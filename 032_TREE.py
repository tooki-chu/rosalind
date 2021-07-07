'''
ROSALIND - Bioinformatics Stronghold
Problem: Completing a Tree
'''

def main():
    with open("datasets/rosalind_tree.txt", "r") as f:
        # total number of nodes
        n = int(f.readline().strip("\n"))
        adj = f.read().strip().split("\n") 
    
        # a tree of n nodes always has n−1 edges
        # just have to deduct the number of edges given in adjacency list
        # to find min number of edges to be added to produce a tree 
        print(n - 1 - adj)


if __name__ == '__main__':
    main()