dna = 'atcgatcgatcgatcgatgtcgctagctagatcgtactcgatcgatgtacgtcgatcgatcgctgaagctagatatcg'
kmer_counts = {}
kmer_length = 4

# the same logic applies for the range, but it depends on the kmer length
for position in range(0 , len(dna) - (kmer_length - 1)):
    # take a slice of the dna string
    kmer = dna[position:position + kmer_length]
    # use get() with a default of 0 
    # the first time we see a given dimer, dimer_counts.get(dimer, 0) will be 0
    # all subsequent times, it will be the value that's current stored
    kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

for kmer, count in kmer_counts.items():
    print(kmer + ' : ' + str(count))    