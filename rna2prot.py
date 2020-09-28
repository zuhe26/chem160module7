from sys import exit
rna=input("Enter RNA string without spaces: ")
# RNA codon dictionary from www.biostars.org/p/2903/
code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"s",
       "UCA":"S", "UCG":"S","UAU":"Y", "UAC":"Y", "UAA":"STOP",
       "UAG":"STOP","UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P",
       "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I",
       "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S",
       "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D",
       "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

protein=""
while len(rna)>=3:
    seq=rna[0:3]
    rna=rna[3:]
    if seq in code:
        if code[seq]=="STOP":
            protein=protein+"STOP"
            break
        protein=protein+code[seq]+"-"
    else: exit("Unknown codon")
print("Protein sequence: ",protein)
if len(rna)>0:
    print("Untranslated RNA: ",rna)
