genetic_code = {
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


def Codons2Protein( ORF, genetic_code ):
    protein = ''
    for i in range( 0, len(ORF), 3 ):
        codon = ORF[i:i+3]
        protein += genetic_code[ codon ]
    return protein



#test Codons2Protein
Codons2Protein( "ATGCTA", genetic_code)

import fasta

infile = 'sce.orf.faa'
outfile = 'sce.protein-translated.faa'

SeqD = fasta.read_fasta2dictionary( infile )

outfl = open(outfile, 'w')

for key in SeqD.keys():
 	orf = SeqD[key]
 	protein = Codons2Protein( orf, genetic_code)
 	header = ">" + key + "\n"
 	outfl.write(header)
 	proteinSeq = protein + "\n"
 	outfl.write(proteinSeq)

outfl.close()
