import fileinput
import os

os.chdir("basic problems")
os.chdir("data")
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
        elif n not in ['A', 'G', 'C', 'T']:
            return "Error: Unknown nucleotide in sequence."
        else:
            count[n] = 1
    return count


with open('rosalind_dna.txt', 'r') as file:      
    DNA1 = file.read().rstrip()
with open('rosalind_dna (1).txt', 'r') as file:
    DNA2 = file.read().rstrip()
    
print("\nProblem 1: Counting DNA nucleotides\n\nTesting using random downloaded DNA sequences from https://rosalind.info/problems/dna/:\n")

print(nucleotide_counter(DNA1))                  ## Testing using random downloaded DNA sequences from https://rosalind.info/problems/dna/
print(nucleotide_counter(DNA2))

print("\nTesting edge cases (s == '', s == 'XXXXX', s == '1234'):\n")

print(nucleotide_counter(""))                     ## Testing edge cases (s == '', s == 'XXXXX', s == '1234')
print(nucleotide_counter("TTTTT"))
print(nucleotide_counter("1234")+"\n")



'''
Problem 2: Transcribing DNA into RNA



'''