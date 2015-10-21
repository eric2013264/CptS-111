#lab7
import string

def cleanup(word):
    word = word.replace(' ','')                            
    word = word.lower();                                  
    return word

input_file = open(input("name of input file: "), 'r')
text = input_file.read()

accumulator = 0

for word in text.split():
	word = cleanup(word)
	if word == "the":
		accumulator = accumulator + 1

print (accumulator)

# to use, place lab7.py on desktop in a file named Lab7

# for it to work, lab7file.txt must be in the file Lab7 as well. (found on cpts site)

# next, copy and paste the following into the terminal.
# cd ~/desktop/Lab7
# python3 lab7.py
# lab7file.txt