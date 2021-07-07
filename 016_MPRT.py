'''
ROSALIND - Bioinformatics Stronghold
Problem: Finding a Protein Motif
'''

import requests
from urllib.request import urlopen
import re

def Uniprot_search(accessIDs):
    """
    Given a list of UniProt access IDs
    
    Returns the corresponding protein sequence for each access ID
    """
    
    # dictionary to store access ID and protein seq
    proteins = {}
    
    for ID in accessIDs:
        # generate url for each uniprot ID
        base_url = "http://www.uniprot.org/uniprot/"
        url = base_url + ID + ".fasta"
        
        # check for redirects
        test = requests.get(url)
        if test.url != url:
            url = test.url
            
        # obtain protein sequence
        response = urlopen(url)
        # converts text from webpage to a string
        page = response.read().decode("utf-8", "ignore")
        # separate header line
        lines = page.split("\n", 1)
        # remove "\n" from protein sequence
        prot = lines[-1].replace("\n", "")
    
        # add entry into dictionary
        proteins[ID] = prot
        
    return proteins


def motif_search(proteins):
    """
    Given a dictionary with access ID as keys and protein seq as values
    
    Returns the access ID and list of locations in the protein string
    where the N-glycosylation motif can be found
    """    
    
    # dictionary to store the access ID and locations of motif
    locations = {}
    
    # create pattern object for pattern matching
    # ?= is important for finding overlapping matches
    motif = re.compile(r"(?=([N][^P][S|T][^P]))")
    
    for ID in proteins:
        seq = proteins[ID]
        
        # find all occurrences of the motif
        # re.findall returns a list with all the matched sequences
        matches = re.findall(motif, seq)
        
        if len(matches) != 0:
            positions = []
            # output the positions in protein string where the motif is found 
            for m in matches:
                for match in re.finditer(m, seq):
                    positions.append(match.start(0) + 1)
            
            locations[ID] = positions
            
    return locations


def main():
    with open('datasets/rosalind_mprt.txt', 'r') as f:
        IDs = f.read().strip().splitlines()
        prot_seqs = Uniprot_search(IDs)
        results = motif_search(prot_seqs)
        
        for protein in results:
            print(protein)
            print(" ".join(str(location) for location in results[protein]))


if __name__ == '__main__':
    main()