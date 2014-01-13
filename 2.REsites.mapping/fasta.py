# Read sequences from a fasta file
# Keep track of headers and sequences
# see page 212 Haddock & Dunn for hints

# 2012 Nov 4, Hong Qin

import re

def read_fasta2dictionary(fastaFileName):
	infl = open( fastaFileName,"r")
	
	debug = 0; 
	
	RecordNum = -1
	Names =[]
	Sequences = []
	
	for Line in infl:
		Line = Line.strip()
		if Line[0]=='>': #Fasta header, a new record
			if( debug>2 ) : print(Line)
			RecordNum += 1
			if( debug ) : print("RecordNum=" + format(RecordNum,"3d") + Line[1:] )
			#Names.append( Line[1: ])
			Line = Line[1:]
			ElementList = re.split('\s+', Line)
			Names.append(ElementList[0])
			Sequences.append("")
		else:
			Sequences[RecordNum] += Line
			if( debug) : print(RecordNum, Sequences[RecordNum])
	
	infl.close()
	
	#print out sequence to check the results
	#for i in range(0, len(Names)):
	#	print( "Name:", Names[i], "\tSequence:", Sequences[i])
		
	MySeqs = dict(zip(Names, Sequences))
	
	#for key in MySeqs.keys():
	#	print(key, MySeqs[key])
	return( MySeqs )
