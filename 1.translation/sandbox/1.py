gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# gencode is defined above
# first let's write a function that will translate a single codon
def translate_codon(codon):
    return gencode.get(codon.upper(), 'x')
# and test it
assert translate_codon('atg') == 'M'
assert translate_codon('GTG') == 'V'
assert translate_codon('banana') == 'x'

# now a function that splits up a DNA string into codons
def split_into_codons(dna):
    codons = []
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        codons.append(codon)
    return codons
# a few tests
assert split_into_codons('atgatgt') == ['atg', 'atg']
assert split_into_codons('atgat') == ['atg']
        
# how about a function that joins a list of animo acids
def join_amino_acids(amino_acids):
    result = ''
    for aa in amino_acids:
        result = result + aa
    return result
# and tests

assert join_amino_acids(['a', 'b', 'c']) == 'abc'

# now we can write our main function
def translate_dna(dna):
    codons = split_into_codons(dna)
    amino_acids = []
    for codon in codons:
        amino_acids.append(translate_codon(codon))
    protein_string = join_amino_acids(amino_acids)
    return protein_string



dna = 'atgcgatcgatcgatcgatgctagctacgtagcatcgatc'
print(translate_dna(dna))