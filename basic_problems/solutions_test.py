from solutions import nucleotide_counter
from solutions import RNA_transcriber
import os

DNA1 = open("data/rosalind_dna.txt", "r").read()
DNA2 = open("data/rosalind_dna (1).txt", "r").read()
RNA1 = open("data/rosalind_rna.txt", "r").read()
RNA2 = open("data/rosalind_rna (1).txt", "r").read()

def test_nucleotide_counter():
    ## Testing using random downloaded DNA sequences from https://rosalind.info/problems/dna/
    assert nucleotide_counter(DNA1) == {'A': 221, 'C': 244, 'G': 222, 'T': 218} 
    assert nucleotide_counter(DNA2) == {'C': 219, 'A': 232, 'T': 236, 'G': 236}
    ## Testing edge cases (s == '', s == 'XXXXX', s == '1234')
    assert nucleotide_counter('') == {}
    assert nucleotide_counter('TTTTT') == {'T': 5}
    assert nucleotide_counter("1234") == "Error: Unknown nucleotide in sequence."

def test_RNA_transciber():
    assert RNA_transcriber(DNA1) == RNA1
    assert RNA_transcriber(DNA2) == RNA2
    assert RNA_transcriber('') == ''
    assert RNA_transcriber('TTTTT') == 'UUUUU'
    assert RNA_transcriber('AAAAA') == 'AAAAA'
    




