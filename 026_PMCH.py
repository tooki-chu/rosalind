'''
ROSALIND - Bioinformatics Stronghold
Problem: Perfect Matchings and RNA Secondary Structures
'''

from math import factorial as fact

def main():
    with open("datasets/rosalind_pmch.txt", "r") as f:
        record = f.read().split()
        rna = record[1]
        
        AUs = rna.count("A")
        GCs = rna.count("G")
        
        print(fact(AUs) * fact(GCs))


if __name__ == '__main__':
    main()