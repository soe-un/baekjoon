N = int(input())
dna = list(input())

DNA_DIC = {
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T",
}

for i in range(N-2, -1, -1):
    dna[i] = DNA_DIC[dna[i] + dna[i + 1]]
    dna.pop()
print(*dna)