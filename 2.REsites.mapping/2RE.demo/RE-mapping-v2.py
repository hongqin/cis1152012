import re, fasta

infile = 'sce.orf-small.faa'
outfile = 'sce.orf-RE-mapping.txt'

#use a function in fasta module to get sequences in Dictionary
SeqD = fasta.read_fasta2dictionary( infile )
# dir(SeqD)

# a function to check sequence pattern in an input sequence
def contains_motif(motif, input):
    if re.search(motif, input.upper()):     
        return True
    else:
        return False

# list of restriction enzymes and their recognition sites
# because these sites are palindromes, we do not need to check the reverse complimentary sequences
enzymes = {
    'test1' : r'GGTA',  #for debug only
    'EcoRI' : r'GAATTC', 
    'BamHI' : r'GGATCC', 
    'BamHI' : r'AGATCT', 
    'XhoI' :  r'CTCGAG', 
    'AccI' :  r'GT[AC][GT]AC',
    'BrsI'  : r'ACTGG[ATGC]'
    }

OUT = open(outfile, 'w')

for k in SeqD.keys(): #loop over sequences
	DNA = SeqD[k]	
	DNA = DNA.upper()
	for REname in enzymes.keys():   #loop over REs
		position = 0
		while contains_motif( enzymes[REname], DNA[ position: ]) :
			result = re.search( enzymes[REname], DNA[position: ] )
			line = k + "\t" + REname + "\t" + enzymes[REname] + format(result.start(), "d")
			position += result.start() + 1  #current position + 1, moving forward by 1 nucleotide
			line = line + '\t' + DNA[ (position-1): (position -1 +len(enzymes[REname]))]
			print( line )
			OUT.write((line+"\n"))
			
