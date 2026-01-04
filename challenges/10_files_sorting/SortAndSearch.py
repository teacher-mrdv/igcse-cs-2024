##
# Python challenge to practice file IO code to showcase the BUBBLE SORT algorithm
# writing different functions according to the prompts
##

def print_data(array: list) -> None:
    for line in array:
        for item in line:
            print(f'{item:10}', end="\t")
        print()
    print()

# 1: read the data from the grades.csv file [subject,grade] and return a 2D array with its data.
# Note that there's no header row
def read_file(filename: str) -> list:
    array: list = []
    with open(filename, 'r') as file:
        for row in file:
            row = row.split(',')
            rowData = []
            rowData.append(row[0])
            rowData.append(float(row[1]))
            array.append(rowData)
    return array

# 2: construct a function to look for a specific subject and output the subject and its corresponding grade,
#       or an error message, like 'subject not found'

# 3: construct a function to save the contents of a 2D array to a given file name

# 4: construct a function to sort the data by subject and save it to a file named 'subjects.csv'

# 5: construct a function to sort the data by grade (descending order) and save it to a file named 'top.csv'

## main
grades: list = read_file('grades.csv')
print_data(grades)