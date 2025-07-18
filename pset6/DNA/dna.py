import sys

def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character for most consecutive runs of subsequence
    for i in range(sequence_length):

        count = 0

        # Check for a subsequence match
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update most consecutive matches
        longest_run = max(longest_run, count)

    return longest_run


# Check for command-line usage
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Read database file into a variable
sequences = []
dnafile = {}

# Open the file
with open(sys.argv[1]) as dictfile:
    # For each line in the file
    for index, row in enumerate(dictfile):
        # If it's the first line
        if index == 0:
            # Get the names of each sequence
            sequences = [
                sequence for sequence in row.strip().split(",")][1:]
        else:
            # Get the name and the DNA sequence
            name = row.strip().split(",")
            dnafile[name[0]] = name[1:]

# Read DNA sequence file into a variable
with open(sys.argv[2], "r") as txtfile:
    sequence = txtfile.read().replace('\n', '')

# Find longest match of each STR in DNA sequence
result = [longest_match(sequence, STR) for STR in sequences]

# Check database for matching profiles
for s in dnafile:
    count = 0

    # for each string
    for j in range(len(dnafile[s])):
        # check if the strings match
        if result[j] == int(dnafile[s][j]):
            # if they do, increase the counter
            count += 1

    # if the counter is equal to the number of sequences
    if count == len(sequences):
        # print the name of the person
        print(s)

print("No match")
