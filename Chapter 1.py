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



#ATCG Count 
