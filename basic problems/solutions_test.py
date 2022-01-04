import solutions
import os

print(os.listdir())



def test_nucleotide_counter():
    assert solutions.nucleotide_counter('') == {'T': 218, 'A': 221, 'G': 222, 'C': 244}
    assert solutions.nucleotide_counter('DNA2') == {'C': 219, 'A': 232, 'T': 236, 'G': 236}
    assert solutions.nucleotide_counter('') == {}
    assert solutions.nucleotide_counter('AAAAA') == {'T': 5}
    assert solutions.nucleotide_counter('1234') == "Error: Unknown nucleotide_counter in sequence."
    