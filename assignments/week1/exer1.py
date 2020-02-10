"""
Exercises on python variables, data structures and control flows

Mode of submission.
 - Create three python files, part1.py, part2.py, part3.py
 - Follow the instructions per part
 - You might need look for some help online.

"""

# ################# PART 1 #################
# Fill in the blank the needed code

name = 'Your name here'
random_decimal = 9.12345678

print(f"My name is {______}")

# Print the decimal using 3 decimal places only
print(f"Decimal with 3 decimal places {______}")


# Change the element in the list to reflect the proper alphabet order
list1 = ['A', 'B', 'C', 'XX', 'E', 'F', 'XX', 'H', 'XX']

# #############################
# Put your code inside the space provided





# #### End code here ##########
print(f"Updated list: {list1}")


# Create a list with 30 pairs of hep hep hooray!
list2 = ['hep hep', 'hooray'] ________
print(list2)




# ################# PART 2 #################
# Create a code that will generate the same image using print


num = input('Enter a number: ')
num = int(num)


"""
A)
num = 5

*
* * 
* * *
* * * *
* * * * *

num = 2

*
* * 

"""


"""
B)
num = 5

     *
    * *
   * * *
  * * * *    
 * * * * *
  * * * *
   * * *
    * *
     *

num = 2

  *
 * *
  *

"""


"""
B)
num = 5

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

num = 2

*  *
****
*  *

"""


# ################# PART 3 #################
# Create a student database record that allows you to store students

# You need to search on how to add new element to a list
# Use student list for the list of students
# Student list is initially filled with one student

student_list = [
	{
		'name': 'Juan',
		'year_level': 8,				# grade 1 - 12
		'age': 12
	}
]

while True:
	opt = input('1) Add student - 2) View all student - 3 Exit')
	opt = int(opt)

	if opt == 3:
		print('Thanks!')
		break

	elif opt == 2:
		if len(student_list) == 0:
			print('Student list is still 0')
			continue

		# Do the priting of student list here
		# Print format

		# Student info
		# Name:
		# Age:
		# Year Level:

		# ##### PUT CODE HERE




		#########################

	elif opt == 1:

		print('Adding student')

		# ##### PUT CODE HERE
		# Ask for 3 info, NAME, YEAR_LEVEL, AGE



		#########################
