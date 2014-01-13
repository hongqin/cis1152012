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


# gencode has already been defined
def translate_codon(codon):
    return gencode.get(codon.upper(), 'x')

def join_amino_acids(amino_acids):
    result = ''
    for aa in amino_acids:
        result = result + aa
    return result

# add a frame parameter
def split_into_codons(dna, frame):
    codons = []
    # all we have to do is modify the start of the range
    for i in range(frame - 1, len(dna)-2, 3):
        codon = dna[i:i+3]
        codons.append(codon)
    return codons
# test the new version
assert split_into_codons('atgatg', 1) == ['atg', 'atg']
assert split_into_codons('atgatg', 2) == ['tga']
assert split_into_codons('atgatg', 3) == ['gat']


# we will add frame to our old function and rename it
def translate_dna_single(dna, frame=1):
    codons = split_into_codons(dna, frame)
    amino_acids = []
    for codon in codons:
        amino_acids.append(translate_codon(codon))
    protein_string = join_amino_acids(amino_acids)
    return protein_string

assert translate_dna_single('atgatg') == translate_dna_single('atgatg', 1)

def translate_dna(dna):
    all_translations = []
    for frame in range(1,4):
        all_translations.append(translate_dna_single(dna, frame))
    return all_translations

dna = 'atgcgatcgatcgatcgatgctagctacgtagcatcgatc'
print(translate_dna(dna))