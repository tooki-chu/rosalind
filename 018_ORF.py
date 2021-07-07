'''
ROSALIND - Bioinformatics Stronghold
Problem: Open Reading Frames
'''

from Bio import SeqIO
from Bio.Seq import Seq

def ORFcandidates(dna):
    """
    Returns every candidate protein string that can be translated
    from ORFs of DNA string given in FASTA format
    """
    
    # stop codons
    STOP = ["TAA","TAG","TGA"]
    
    # original strand
    forward = dna.seq
    
    # reverse complement strand
    reverse = forward.reverse_complement()
    
    # store unique protein strings
    candidates = set()
    
    for strand in [forward, reverse]:
        # check all possible reading frames
        for i in range(len(forward)-2):
            
            # look for start codon
            if strand[i:i+3] == 'ATG':
                # construct substring
                substring = strand[i:]
                
                # check for stop codon
                for j in range(i, len(substring), 3):
                    if substring[j:j+3] in STOP:
                        P = substring.translate(to_stop=True)
                        candidates.add(str(P))
                        break

    return candidates


def main():
    with open('datasets/rosalind_orf.txt', 'r') as f:
        DNA = SeqIO.read(f, "fasta")
        proteins= ORFcandidates(DNA)
        print("\n".join(proteins))



if __name__ == '__main__':
    main()