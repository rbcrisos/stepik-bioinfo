## Functions needed for Bioinformatics

def PatternCount(Text, Pattern):
    """
    Counts how many Pattern in Text
    input: 
    text = "ATGCACACTTCGATCTGGACTGACTGGACGGAGAGCGGCTTAGGAGCTATTC"
    pattern = "AG"

    output: 4
    
    """
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def PatternMatching(Pattern, Genome):
    """
    Finds the position(s) of Pattern in the Genome
    """
    positions = [] #output var
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def FrequencyMap(Text, k):
    """
    Maps and counts how many times a k-mer is in Text
    """
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] += 1
    return freq

def FrequentWords(Text, k):
    """
    Finds the most frequent k-mer(s) in Text
    """
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

def ReverseComplement(Pattern):
    """
    Takes Reverse() and Complement() and reverses then finds the complement of Pattern
    """
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    """
    Reverses Pattern
    """
    reverse = ''.join(reversed(Pattern))
    return reverse

def Complement(Pattern):
    "Uses dictionary of basepairs -key/value and finds the complements of Pattern"
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement


#text = "ATGCACACTTCGATCTGGACTGACTGGACGGAGAGCGGCTTAGGAGCTATTC"
#pattern = 3
#print(FrequentWords(text,pattern))

print(ReverseComplement("GCTAGCT"))

#print(FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3))