import re

def contains_motif(motif, input):
    if re.search(motif, input.upper()):     
        return True
    else:
        return False
    
# I have added some whitespace here to make it easier to see 
enzymes = {
           'ecori' : r'GAATTC', 
           'avaii' : r'GG(A|T)CC', 
           'hsp92i': r'G(A|G)CG(T|C)C',
           'hhai'  : r'GCGC',
           'brsi'  : r'ACTGG[ATGC]'
           }

# notice how we have two nested for loops - one for sequences, one for enzymes
# this is very common - think of it as a series of pairwise comparisons
# each sequence must be tested against each enzyme
input_file = open('3.txt')
for line in input_file:
    split_line = line.rstrip('\n').split(' ')
    name = split_line[0]
    sequence = split_line[1]
    print(name)
    for enzyme_name, motif in enzymes.items():
        if contains_motif(motif, sequence):
            print('  contains ' + enzyme_name)
        
        
# hopefully it is obvious from looking at the script that if we want to add
# more enzymes, all we have to do is alter the enzymes dict. None of the other
# code has to change