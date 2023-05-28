'''
Problem:
The problem involves finding the second lowest degree in a nested list and printing the names in ascending alphabetical order if there are multiple names with the same degree.
'''
python_students = [
	['Harry', 37.21], 
	['Berry', 37.21],
	['Marry', 37.21],
	['Tina', 37.2], 
	['Akriti', 41], 
	['Harsh', 39]
]
#Sort List Based on Degrees
#Exclude The Lowest Degree
#Isolate The Second Lowest Degree/s
#Print Name of Student/s of those degrees ascending alphabetically.

sorted_by_degree = sorted(python_students, key=lambda x: x[1])
lowest_degree = sorted_by_degree[0][1]
second_lowest = None

for student in sorted_by_degree:
	if student[1] > lowest_degree:
		second_lowest = student[1]
		break

names = []

for student in sorted_by_degree:
	if student[1] == second_lowest:
		names.append(student[0])

sorted_names = sorted(names)
for name in names:
	print(name)
	
