'''
ROSALIND - Bioinformatics Stronghold
Problem: Finding a Motif in DNA
'''

def repeats(s, t):
    """
    Returns a list of the starting indices of all occurrences of
    t as a substring of string s
    """
    
    # length of substring
    l = len(t)
    
    for char in s:
        locations = [i+1 for i in range(len(s)) if s[i:i+l] == t]
     
    return locations


def main():
    with open('datasets/rosalind_subs.txt', 'r') as f:
        s, t = f.read().strip().split("\n")
        print(*repeats(s,t))

if __name__ == '__main__':
    main()