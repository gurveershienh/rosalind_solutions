'''
Problem 1: DNA nucleotide counter

Deoxyribose nucleic acid (DNA) is a polymer comprised of four different nucleic acids, or nucleotides. 
These 4 nucleotides are adenine (A), guanine (G), thymine (T), and cytosine (C).

'''

def nucleotide_counter(file):
    '''
    Returns the number of occurences for each nucleotide given a DNA sequence.

    nucleotide_counter: Str -> dictof(Str, Nat)

    where Str ∈ ['A', 'G', 'C', 'T'] and len(s) <= 1000

    '''
    s = open(file, "r").read()
    count = {}
    for n in s:
        if n in count:
            count[n] += 1
        elif n not in ["A", "G", "T", "C"]:
            return "Error: Unknown nucleotide in sequence."
        else:
            count[n] = 1
    return count

'''
Problem 2: Transcribing DNA into RNA

Ribose nucleic acid (RNA) is the second nucleic acid in living organisms. 
DNA serves as a blueprint for RNA sequences, where every thymine (T) nucleotide
in a transcripted RNA is replaced by A uracil (U) nucleotide.

'''

def RNA_transcriber(file):
    '''
    Returns the RNA transcription of DNA (every T replaced with U)
    
    RNA_transcriber: Str -> Str
    
    Where Str ∈ ['A', 'G', 'C', 'T'] and len(s) <= 1000
    
    '''
    s = open(file, "r").read()
    return s.replace("T", "U")


'''
Problem 3:
'''

def reverse_complement(file):
    '''
    Returns the reverse complement of a given DNA with >1000bp
    
    '''
    s = open(file, "r").read()
    rev_comp = ''
    for i in  reversed(s):
        if i == 'A':
            rev_comp += "T"
        elif i == 'T':
            rev_comp +="A"
        elif i == 'C':
            rev_comp += "G"
        else:
            rev_comp += "C"
    return rev_comp

'''
Problem 3: Determining unknown DNA

'''

def gc_content(file):
    s = open(file, "r").read()
    gc_dict = {}
    i = 0
    while s[i] != "\n":
        i += 1
    i -= 1
    for seq in s[1:].replace("\n",'').split(">"):
        gc = (seq[i:].count('G') + seq[i:].count("C")) / len(seq[i:]) * 100
        fasta = seq[:i]
        gc_dict[fasta] = gc
    ind = list(gc_dict.values()).index(max(gc_dict.values()))
    return list(gc_dict.keys())[ind]



def hamming_distance(file):
    s = open(file, "r").read()
    seq1 = s.split("\n")[0]
    seq2 = s.split("\n")[1]
    count = 0
    for a, b in zip(seq1,seq2):
        if a != b:
            count += 1
    return count

def motif_locator():
    seq = "GGTCCGAGG"
    motif = "AGG"
    for i in range(len(seq)):
        if seq[i:].startswith(motif):
            print(i+1)