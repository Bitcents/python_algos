# This is an example from the book Classic Computer Science Problems in Python
# This script searches for a specific codon within a gene sequence

from enum import IntEnum
from typing import Tuple, List

# Gene sequences are made up of 4 types of nucleotides: 'A', 'C', 'G', 'T'
# We store the nucleotides in an IntEnum, as these won't change throughout the script
# IntEnum also allows us to make comparisons like < > >= and so on 

Nucleotide: IntEnum = IntEnum('Nucleotid', ('A', 'C', 'G', 'T'))

# A codon can be defined as a tuple of three nucleotides
# A gene can be defined as a list of codons

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # type alias for codons
Gene = List[Codon] # type alias for genes

# Genes are usually expressed as strings 
# We need to convert genes from the string form to the Gene type we defined
# This will be done by the function below
def string_to_gene(s:str) -> Gene:
    gene: Gene = []
    
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # we do not want to go out of the string!
            return gene
        try:
            codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
            gene.append(codon) # don't forget to add the codon to the gene
        except KeyError:
            print(f'Invalid character {s[i]} detected in gene sequence at {i+1}th position.')
            print('Returning the partial gene sequence')
            return gene

    return gene # successfully converted gene from string to gene type


# We want to search the gene sequence for a particular codon
# There are several ways to implement this functionality
# We frst look at the simple linear search
# Here, we go through each codon and check if it matches with our target codon
# If there is a match, we return True, or return False otherwise
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
   
    for codon in gene:  # iterating through every codon
        if codon == key_codon:
            return True
    
    return False # returns False by default


if __name__=='__main__':
    gene_str =  "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    test_gene: Gene = string_to_gene(gene_str)
    test_codon: Codon = (Nucleotide['T'],Nucleotide['C'],Nucleotide['T'])
    difference = test_gene[1] > test_gene[0]
    print(difference)