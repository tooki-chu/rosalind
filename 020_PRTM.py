'''
ROSALIND - Bioinformatics Stronghold
Problem: Calculating Protein Mass
'''

def monoisotopic_mass(P):
    """
    Returns total weight of protein P using
    monoisitopic mass of each amino acid residue
    (does not consider the mass of water)
    """
    
    # monoisotopic mass of each amino acid
    mass_table = {'A': 71.03711,'C': 103.00919,'D': 115.02694,'E': 129.04259,
                  'F': 147.06841,'G': 57.02146,'H': 137.05891,'I': 113.08406,
                  'K': 128.09496,'L': 113.08406,'M': 131.04049,'N': 114.04293,
                  'P': 97.05276,'Q': 128.05858,'R': 156.10111,'S': 87.03203,
                  'T': 101.04768,'V': 99.06841,'W': 186.07931,'Y': 163.06333}

    total = sum(mass_table[aa] for aa in P)
    
    return total


def main():
    with open('datasets/rosalind_prtm.txt', 'r') as f:
        protein = f.read().strip()
        print(round(monoisotopic_mass(protein), 3))


if __name__ == '__main__':
    main()