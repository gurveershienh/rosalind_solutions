DNA1 = open("data/rosalind_dna.txt", "r").read()
DNA2 = open("data/rosalind_dna (1).txt", "r").read()
'''
Problem 1: DNA nucleotide counter

Deoxyribose nucleic acid (DNA) is a polymer comprised of four different nucleic acids, or nucleotides. 
These 4 nucleotides are adenine (A), guanine (G), thymine (T), and cytosine (C).

'''

def nucleotide_counter(s):
    '''
    Returns the number of occurences for each nucleotide given a DNA sequence.

    nucleotide_counter: Str -> dictof(Str, Nat)

    where Str ∈ ['A', 'G', 'C', 'T'] and len(s) <= 1000

    '''
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

def RNA_transcriber(s):
    '''
    Returns the RNA transcription of DNA (every T replaced with U)
    
    RNA_transcriber: Str -> Str
    
    Where Str ∈ ['A', 'G', 'C', 'T'] and len(s) <= 1000
    
    '''
    return s.replace("T", "U")

print(RNA_transcriber(DNA1))
