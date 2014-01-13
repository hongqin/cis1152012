# Read sequences from a fasta file
# Keep track of headers and sequences
# see page 212 Haddock & Dunn for hints

# 2012 Nov 4, Hong Qin


import fasta, protein

infl = "peptide2.faa"

SeqD = fasta.read_fasta2dictionary( infl )

outfl = open( "outMW2.txt","w")

for key in SeqD.keys():
	MW = protein.protein_MW( SeqD[key] )
	outfl.write( key + "\t" + format( MW, "7.1f") + "\n")

outfl.close()
