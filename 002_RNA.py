'''
ROSALIND - Bioinformatics Stronghold
Problem: Transcribing DNA into RNA
'''

def transcribe(s):
    """
    Returns transcribed RNA string of a given DNA string
    """

    return s.replace('T', 'U')


def main():
    with open('datasets/rosalind_rna.txt', 'r') as f:
        dna = f.read()

    print(transcribe(dna))

if __name__ == '__main__':
    main()
    
