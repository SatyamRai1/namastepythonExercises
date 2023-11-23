# 1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.
#
# example :
# file 1:
# this is namaste sql course
# this is python course
# this assinment is part of day4 lecture
#
#
# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7


f1 = open("testfile1.txt", "a")

lines = []

ipt = 'y'
while ipt == 'y':
	lines.append(input("Please enter a line of text: "))
	ipt = input("Want to enter more text? y/n: ").lower()

for line in lines:
	f1.write(line + '\n')









f1.close()



