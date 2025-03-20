# Program to eliminate repeated lines from a file 

# creating the output file
outputFile = open('Repeated.txt', "w")

# reading the input file
inputFile = open('UpdatedFile.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines...")
# iterating each line in the file
for line in inputFile:

    # checking if line is unique
    if line not in lines_seen_so_far:

        #write unique lines in input file
        outputFile.write(line)

# closing the file
inputFile.close()
outputFile.close()        