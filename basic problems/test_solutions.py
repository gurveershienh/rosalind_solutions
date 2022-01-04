import solutions
import os

print(os.listdir())

with open('rosalind_dna.txt', 'r') as file:      
    DNA1 = file.read().rstrip()
with open('rosalind_dna (1).txt', 'r') as file:
    DNA2 = file.read().rstrip()

def test_nucleotide_counter():
    assert solutions.nucleotide_counter(DNA1) == {'T': 218, 'A': 221, 'G': 222, 'C': 244}
    assert solutions.nucleotide_counter(DNA2) == {'C': 219, 'A': 232, 'T': 236, 'G': 236}
    assert solutions.nucleotide_counter('') == {}
    assert solutions.nucleotide_counter('AAAAA') == {'T': 5}
    assert solutions.nucleotide_counter('1234') == "Error: Unknown nucleotide_counter in sequence."
    