#Frequent Words Problem
#Given a string TEXT and an integer k return All of the most frequent k-mers in TEXT

def PatternCount(text, pattern):
  count = 0 
  for i in range(0, len(text):
    if text(i, pattern) == pattern:
      count += 1 
   return count 


def FrequentWords(text, k):
  Frequent_Pattern = []
  for i = range(0,len(text)):
    pattern = the k-mer text(i,k)
    Count(i) = PatternCount(text, Pattern)
    
    
    
#Reverse Complement Problem 
#Input a DNA string pattern and return the reverse complement 

def Reverse_complement(dna):
    complement = ''
    for i in dna:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'C':
            complement += 'G'
        else:
            complement += 'C'
    return complement 

#nucleotide Count 

def counts(dna):
    count_A = dna.count('A')
    count_T = dna.count('T')
    count_G = dna.count('G')
    count_C = dna.count('C')

    return count_A, count_C, count_G, count_T
                 
                 
#HammingCount 

                 
def Hamming_distance(str1, str2):
    count = 0
    if len(str1) == len(str2)
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                count += 1
    return count
