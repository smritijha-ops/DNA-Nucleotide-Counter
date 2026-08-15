#DNA Nucleotide Counter

sequence = input("Enter a DNA sequence: ").upper()

#Check whether the sequnce contains only valid DNA bases
if all(base in "ATGC" for base in sequence):
  print("A:", sequence.count("A"))
  print("T:", sequence.count("T"))
  print("G:", sequence.count("G"))
  print("C:", sequence.count("C"))
else:
  print("Invalid DNA sequence. Please use only A, T, G and C.")
