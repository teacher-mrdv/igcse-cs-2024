##
# Python challenge to practice file IO code to showcase the BUBBLE SORT algorithm
# writing different functions according to the prompts
##

# output the 2D array on screen nicely formatted; note that here we are not using indexes
def print_data(array: list) -> None:
    for line in array:
        for item in line:
            print(f'{item:10}', end="\t")
        print()
    print()

# Read the data from the grades.csv file [subject,grade] and return a 2D array with its data.
# Note that there's no header row in the data (csv) file, to make life easier.
def read_file(filename: str) -> list:
    array: list = []
    with open(filename, 'r') as file:
        for row in file:
            # first we create a list from the row/line read from the file (string/raw data);
            row_to_list: list = row.split(',')    # elements are split by a ',' (csv)
            rowData: list = []                    # we create another list to put the data with expected data types
            rowData.append(row_to_list[0])        # leave subject name as string
            rowData.append(float(row_to_list[1])) # but the grade should be converted to a float
            array.append(rowData)                 # add the row to the 2D array (list)
    return array

# 1: construct a function to look for a specific subject and output the subject and its corresponding grade,
#       or an error message, like 'subject not found'

# 2: construct a function to save the contents of a 2D array to a given file name

# 3: construct a function to sort the data by subject and save it to a file named 'subjects.csv'

# 4: construct a function to sort the data by grade (descending order) and save it to a file named 'top.csv'

## main
grades: list = read_file('grades.csv')
print_data(grades)