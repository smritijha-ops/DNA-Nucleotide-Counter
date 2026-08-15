def count_nucleotides(dna_sequence):
    seq = dna_sequence.upper()
    
    # Check whether the sequence contains only valid DNA bases
    if not all(base in "ATGC" for base in seq):
        raise ValueError("Invalid DNA sequence. Please use only A, T, G, and C.")
    
    # Dictionary to store counts
    counts = {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }
    
    return counts

if __name__ == "__main__":
    user_input = input("Enter a DNA sequence: ")
    
    try:
        result = count_nucleotides(user_input)
        print("\nNucleotide Counts:")
        for base, count in result.items():
            print(f"{base}: {count}")
    except ValueError as e:
        print(e)
