# start with 0 for all bases
base_counts = {'a' : 0, 'c' : 0, 't': 0, 'g' : 0}
dna = 'atcgatcgatcgatcgatgtcgctagctagatcgtactcgatcgatgtacgtcgatcgatcgctgaagctagatatcg'

# the left side of an = is always executed first, then the result is stored in the right side
# hence we are allowed to use the same variable on both sides
for base in dna:
    base_counts[base] = base_counts[base] + 1
    
for base, count in base_counts.items():
    print(base + ' : ' + str(count))