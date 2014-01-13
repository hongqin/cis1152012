# for dimers, it would be tedious to write them all out
# so we will just start with an empty dict and add them as we go
dna = 'atcgatcgatcgatcgatgtcgctagctagatcgtactcgatcgatgtacgtcgatcgatcgctgaagctagatatcg'
dimer_counts = {}

# we will start at the first base, but we need to finish at the second-to-last base
# because we need two bases for each time round the loop
for position in range(0,len(dna)-1):
    # take a slice of the dna string
    dimer = dna[position:position+2]
    # use get() with a default of 0 
    # the first time we see a given dimer, dimer_counts.get(dimer, 0) will be 0
    # all subsequent times, it will be the value that's current stored
    dimer_counts[dimer] = dimer_counts.get(dimer, 0) + 1

for dimer, count in dimer_counts.items():
    print(dimer + ' : ' + str(count))    