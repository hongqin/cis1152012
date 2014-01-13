# Read sequences from a fasta file
# Keep track of headers and sequences
# see page 212 Haddock & Dunn for hints

# 2012 Nov 4, Hong Qin

Usage = """6e.calculateMW inputfastafile outputfile """

import fasta, protein, sys

if len(sys.argv) < 2:
    print(Usage)
 
print("::: Read from ", sys.argv[1], " and output MW to ", sys.argv[2])

infl = sys.argv[1]

SeqD = fasta.read_fasta2dictionary( infl )

outfl = open( sys.argv[2], 'w')

for key in SeqD.keys():
	MW = protein.protein_MW( SeqD[key] )
	outfl.write( key + "\t" + format( MW, "7.1f") + "\n")

outfl.close()
