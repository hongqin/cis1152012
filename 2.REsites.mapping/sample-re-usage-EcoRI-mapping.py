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
#    'test1' : r'AA', 
#    'test2' : r'TA', 
    'EcoRI' : r'GAATTC', 
    'BamHI' : r'GGATCC', 
    'BamHI' : r'AGATCT', 
    'XhoI' :  r'CTCGAG', 
    'AccI' :  r'GT[AC][GT]AC',
    'BrsI'  : r'ACTGG[ATGC]'
    }


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
			print( line )
			position += result.start() + 1
			light = contains_motif( enzymes[REname], DNA[ position: ])
			
			
			
			
			#alternative approach, use compiled patterns
cpattern = re.compile('GAATTC')
result = cpattern.search(DNA, 0) #starting at position 0
result.start()
result2 = cpattern.search(DNA, (result.start()+1) )
result2.start()


		currentDNA = DNA
		while (currentDNA.find(REs[RE]) != -1 ):
			results = re.search(REs[RE], DNA)
			line = k + "\t" + RE + format(results.start(), "7d")
			print(line)


for line in input_file:
    split_line = line.rstrip('\n').split(' ')
    name = split_line[0]
    sequence = split_line[1]
    print(name)
    for enzyme_name, motif in enzymes.items():
        if contains_motif(motif, sequence):
            print('  contains ' + enzyme_name)
    

for k in SeqD.keys():
	DNA = SeqD[k]	
	DNA = DNA.upper()
	for RE in REs: 
		currentDNA = DNA
		while (currentDNA.find(REs[RE]) != -1 ):
			results = re.search(REs[RE], DNA)
			line = k + "\t" + RE + format(results.start(), "7d")
			print(line)
			currentDNA = 
	
	
	
	#alternative approach, use compiled patterns
cpattern = re.compile('GAATTC')
result = cpattern.search(DNA, 0) #starting at position 0
result.start()
result2 = cpattern.search(DNA, (result.start()+1) )
result2.start()


			
result.start()
rL.append(result.start())
DNA[6:12]
result = re.search(pattern, DNA[rL[0]+1:])
result.start()
rL.append(result.start()+rL[0]+1)




#       01234567890 123456789 01234567
Line = "Dec-01-2012\t1.0 mile\t5.0 min"
SearchStr = '([\d\.]+) mile\t([\d\.]+) min'
Result = re.search(SearchStr, Line)
dir(Result)
Result.start()

print(Result.groups()) #all result
Result.group(1)  #by group
Result.group(2)
print("Average speed=", float(Result.group(1))/float(Result.group(2)) )
Newstring = Result.group(2) + " " + Result.group(1)


SearchStr = r'[\d\.]+' #for raw pattern
Result = re.findall(SearchStr,Line)
print(Result)
print(Line)

Header = ">YAL001C TCF3 SGD001 Chr I"
SearchStr = '>(\w{3}\d{3}\w+) (\w{3})'
SearchStr = '>(\w{3}\d{3}\w+) (\w+)'
Result = re.search(SearchStr, Header)
Result.group(2)


# map EcoRI GAATTC site in DNA
pattern = 'GAATTC'
DNA = "atcgatGAATTCttagtaattGAATTCtactag"
#      012345678901234567890123456789012
DNA = DNA.upper()
rL=list() #store RE sites

result = re.search(pattern, DNA)
result.start()
rL.append(result.start())
DNA[6:12]
result = re.search(pattern, DNA[rL[0]+1:])
result.start()
rL.append(result.start()+rL[0]+1)

#results = re.findall(pattern, DNA), does not seem to work

#alternative approach, use compiled patterns
cpattern = re.compile('GAATTC')
result = cpattern.search(DNA, 0) #starting at position 0
result.start()
result2 = cpattern.search(DNA, (result.start()+1) )
result2.start()


