genome = "aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga"

genome = genome.upper()

def PatternMatching(Pattern, Genome):
    """
    Finds the position(s) of Pattern in the Genome
    """
    positions = [] #output var
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

#print(genome)

pattern_1 = "ATGATCAAG"
pattern_2 = "CTTGATCAT"
#pattern_3 = "GCG"
#genome_2 = "GCGCG"

count_1 = len(PatternMatching(pattern_1, genome))
count_2 = len(PatternMatching(pattern_2, genome))

print(count_1 + count_2)
