from sys import exit 
file_path = input("Path to DNA Sequence: ")
try: 
    with open(file_path, "r") as file: 
        text = file.read().strip()
        print(text)
except FileNotFoundError: 
    print("File cannot be found")
    exit()

nucleotides = {"A":0, "T":0, "C":0, "G":0}
for char in text:
    if char in nucleotides: 
        nucleotides[char] += 1
    else: 
        print("Error: Invalid nucleotide")
        exit()
print("Nucleotide Count", nucleotides)

GC = ((nucleotides["C"] + nucleotides["G"])/len(text)) * 100
print("GC Content:", GC)

def complement_strand(text): 
    complement_strand = ""
    for char in text: 
        if char == "A": 
            complement_strand += "T"
        elif char == "T": 
            complement_strand += "A"
        elif char == "G": 
            complement_strand += "C"
        elif char == "C": 
            complement_strand += "G"
        else: 
            complement_strand += char 
    return(complement_strand)
print("Complementary Strand:", complement_strand(text))

def translate_RNA(complement_strand):
    translate_RNA = ""
    for char in complement_strand: 
        if char == "T": 
            translate_RNA += "U"
        else: 
            translate_RNA += char
    return(translate_RNA)
print("Translation into RNA:", translate_RNA(complement_strand(text)))
    