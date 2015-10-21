#lab6

input_file_name = input("name of input file: ")

# Read the file into a string
input_file = open(input_file_name, 'r')
text = input_file.read()

print ("\n")
print ("contents of input file: ", "\n", text)

outfile_name = input("name of output file: ")

# Split into lines
text = text.split('\n')

# Sort the list of lines
text.sort()
text.reverse()

# Write each of the lines in turn into a file
outfile = open(outfile_name, 'w+')
for line in text:
	outfile.write(line + '\n')

outfile.close()

print ("\n")
print ("success!")

#cd ~/desktop/Lab6
#python3 lab6.py