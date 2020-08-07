'''
ROSALIND - Bioinformatics Stronghold
Problem: Calculating Expected Offspring
'''

def phenotype(parents, dominant=True, offspring=2):
    """
    Returns the expected number of offspring that display the 
    dominant/recessive phenotype in the next generation
    
    Default assuption that every couple has exactly 2 offspring
    
    Genotypes of parents should be provided in this order:
    1. AA - AA
    2. AA - Aa
    3. AA - aa
    4. Aa - Aa
    5. Aa - aa
    6. aa - aa
    """
    
    # dominant phenotype
    if dominant:
        ratios = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

    # recessive phenotype    
    else:
        ratios = [0.0, 0.0, 0.0, 0.25, 0.5, 1.0]

    nxt_gen = sum([x[0] * x[1] for x in zip(parents, ratios)]) * offspring 
    
    return nxt_gen


def main():
    with open('datasets/rosalind_iev.txt', 'r') as f:
        parents = [int(i) for i in f.read().split()]
        print(phenotype(parents))


if __name__ == '__main__':
    main()