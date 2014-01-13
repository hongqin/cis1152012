import re, fasta,  sys

infile = 'sce.orf-small.faa'
outfile = 'sce.orf-RE-mapping.txt'

SeqD = fasta.read_fasta2dictionary( infile )
dir(SeqD)

def contains_motif(motif, input):
    if re.search(motif, input.upper()):     
        return True
    else:
        return False

enzymes = {
    'test1' : r'GGTA', 
    'test2' : r'GGGG', 
    'EcoRI' : r'GAATTC', 
    'BamHI' : r'GGATCC', 
    'BamHI' : r'AGATCT', 
    'XhoI' :  r'CTCGAG', 
    'AccI' :  r'GT[AC][GT]AC',
    'BrsI'  : r'ACTGG[ATGC]'
    }

OUT = open(outfile, 'w')

for k in SeqD.keys():
	DNA = SeqD[k]	
	DNA = DNA.upper()
	for REname in enzymes.keys():   #REname = 'test1'
		light = contains_motif( enzymes[REname], DNA )
		#cpattern = re.compile( enzymes[REname] )
		position = 0
		while light :
			result = re.search( enzymes[REname], DNA[position: ] )
			line = k + "\t" + REname + "\t" + enzymes[REname] + format(result.start(), "7d")
			position += result.start() + 1  #current position
			line = line + '\t' + DNA[ (position-1): (position+len(enzymes[REname])-1)]
			print( line )
			OUT.write((line+"\n"))
			light = contains_motif( enzymes[REname], DNA[ position: ])
			
