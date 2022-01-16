from solutions import nucleotide_counter
from solutions import RNA_transcriber
from solutions import gc_content


RNA1 = open("data/rosalind_rna.txt", "r").read()        ##Rosalind confirmed answers to Problem #2
RNA2 = open("data/rosalind_rna (1).txt", "r").read()
GC_1 = "Rosalind_3245"                                  ##Rosalind confirmed answers to Problem #6
GC_2 = "Rosalind_9972"
GC_3 = "Rosalind_1974"

def test_nucleotide_counter():
    ## Testing using random downloaded DNA sequences from https://rosalind.info/problems/dna/
    assert nucleotide_counter("data/rosalind_dna.txt") == {'A': 221, 'C': 244, 'G': 222, 'T': 218} 
    assert nucleotide_counter("data/rosalind_dna (1).txt") == {'C': 219, 'A': 232, 'T': 236, 'G': 236}

def test_RNA_transciber():
    ## Testing using random downloaded DNA sequences from https://rosalind.info/problems/dna/
    assert RNA_transcriber("data/rosalind_dna.txt") == RNA1
    assert RNA_transcriber("data/rosalind_dna (1).txt") == RNA2
    
def test_gc_content():
    assert gc_content("data/rosalind_gc.txt") == GC_1
    assert gc_content("data/rosalind_gc (1).txt") == GC_2
    assert gc_content("data/rosalind_gc (2).txt") == GC_3
