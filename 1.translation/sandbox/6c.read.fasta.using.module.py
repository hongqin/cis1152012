# Read sequences from a fasta file
# Keep track of headers and sequences
# see page 212 Haddock & Dunn for hints

# 2012 Nov 4, Hong Qin


import fasta

infl = "peptide2.faa"

SeqD = fasta.read_fasta2dictionary( infl )

for key in SeqD.keys():
	print(key, SeqD[key])

