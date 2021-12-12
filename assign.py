	#Create a program that will allow a user to do either of the following things:
	# Get input from the user to write the following information to a file:
	#Student name
	#Assignment average grade
	#Midterm exam grade
	#Final project grade
	#Final exam grade
	#Allow the user to search the file by student name and output a weighted average (15%, 25%, 25%, and 35%, 
	#respectively) based on the grades for that student in the file.
	#The user should be able to choose either of the two options until they want to stop.

add_student = 'Y'
info = open('StudentData.txt', 'a')


while (add_student == 'Y' or add_student == 'y'):
	name = input("Please enter the students name")
	assignment_avg = input("Please enter the students assignment average grade")
	midterm_grade = input("Please enter the students Midterm average grade")
	final_project = input("Please enter the students Final project grade")
	final_exam = input("Please enter the students Final Exam grade")

	info.write(name+"\n")
	info.write(assignment_avg+"\n")
	info.write(midterm_grade+"\n")
	info.write(final_project+"\n")
	info.write(final_exam+"\n")

	add_student = input("Do you want to add another student? Y/N")
info.close()	

again = 'Y'

while again == 'Y' or again == 'y':
	file = open('StudentData.txt', 'r')
	name_search = input("What student do you want to pull records for?")
	again = 'Y'
	match = False


	line = file.readline().rstrip()	

	while line!='':
		names = line 
		a_avg = file.readline().rstrip()
		m_grade = file.readline().rstrip()
		f_proj = file.readline().rstrip()
		f_exam = file.readline().rstrip()

		if name_search == line:
			weighted_average = (float(a_avg) * .15) + (float(m_grade) * .25) + (float(f_proj) * .25) + (float(f_exam) * .35)
			print("The average for this student is", weighted_average)
			match = True
	        
		line = file.readline().rstrip()

	file.close()

	if match == False:
	    print("No information found")

	again = input("Do you want to search another student? Y/N")
