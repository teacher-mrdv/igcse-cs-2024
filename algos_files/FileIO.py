##
# Python example code to showcase File input and output in Python,
# as required by our IGCSE syllabus
# The file is in CSV format, hbdata.csv, with the following headers/variables/data:
# 0           1             2      3                      4   <---index
# student_id, student_name, grade, homebase_teacher_name, homebase_room
##
import copy		# to copy arrays easily--how would you copy 1D & 2D arrays manually?

# The following constants are for ease of use/accessing specific data
STUDENT_ID = 0
STUDENT_NAME = 1
GRADE = 2
HOMEBASE_TEACHER_NAME = 3
HOMEBASE_ROOM = 4

def print_data(array: list) -> None:
    headers: list = ['STUDENT ID', 'STUDENT NAME', 'GRADE', 'HOMEBASE TEACHER NAME', 'HOMEBASE ROOM']
    for header in headers:
        print(f'{header:20}', end="\t")
    print()
    for line in array:
        for item in line:
            print(f'{item:20}', end="\t")
        print()
    print()

# sorts a 2D array by a chosen column. Look at the constants above.
# note that the algorithm is the same, but we move entire rows
def bubble_sort2D(array_data: list, column: int) -> list:
    array: list = copy.deepcopy(array_data)		# we have to do this in Python to leave the original array unmodified
    swapped: bool = True
    passes: int = 0
    while swapped:
        swapped = False
        index: int = 0
        for index in range(len(array) - 1 - passes):
            if array[index][column] > array[index + 1][column]:
                temp: list = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                swapped = True
    return array

# reads a file (csv) and returns a 2D array/list with the contents of the CSV file
def read_data(filename: str) -> list:			# read the contents of filename and store them in an array [list]
    data: list = []
    with open(filename, 'r') as dataFile:		# open the file for reading operations
        for line in dataFile:
            line = line.rstrip()                # remove trailing whitespace[s] from the end of a string
            parsed_data: list = line.split(',') # splits each CSV line into a 2D array/list
            data.append(parsed_data)
        data.pop(0)                             # remove the header of the CSV file
    #print_data(data)                           # optional, can be removed/commented out
    return data

# writes a CSV file with the contents of a 2D array/list
def write_data(filename: str, array: list) -> None:
    with open(filename, 'w') as dataFile:
        for line in array:
            line_to_write: str = ''
            for item in line:
                line_to_write += item + ','
            line_to_write = line_to_write[:len(line_to_write)-1] # remove the last comma
            dataFile.write(line_to_write + '\n')# add a newline '\n' at the end of each line 
            #print(line_to_write)               # optional, can be removed/commented out
    print(f'\n>>>{filename} saved successfully.')

# main
homebase_data: list = read_data('homebases.csv')
homebase_data = bubble_sort2D(homebase_data, GRADE)
print_data(homebase_data)
write_data('homebases_by_grade.csv', homebase_data)

homebase_data: list = read_data('homebases.csv')
homebase_data = bubble_sort2D(homebase_data, HOMEBASE_TEACHER_NAME)
print_data(homebase_data)
write_data('homebases_by_teacher.csv', homebase_data)

# Read the code and analyse it carefully, we will discuss it in class

