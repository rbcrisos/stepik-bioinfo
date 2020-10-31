
v_cholerae = '''
CTTGATCATCTTGATCATCTTGATCAT
'''


def PatternMatching(Pattern, Genome):
    """
    Finds the position(s) of Pattern in the Genome
    """
    positions = [] #output var
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

pattern_gn = "CTTGATCAT"

pattern_m = PatternMatching(pattern_gn, v_cholerae)

print(pattern_m)