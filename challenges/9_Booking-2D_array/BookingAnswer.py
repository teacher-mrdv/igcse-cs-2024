##########################################################################
# Write a program that meets the following requirements:
### counts and outputs the number of seats already booked for the evening
### allows the user to input the number of seats required
### validates the input
### checks if enough seats are available:
###### if they are available
######### changes the status of the seats
######### outputs the row number and seat number for each seat booked
###### if they are not available:
######### outputs a message giving the number of seats left or
######### 'House full' if the theatre is fully booked.
##########################################################################

# Booking problem given 2D array data - global variable
evening = [ [True, True, True, False, True, False, False, False, True, True, True, False, False, False, False, True, False, False, False, True],
            [True, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, False, False, False, True],
            [True, False, True, True, False, True, False, False, False, False, False, True, False, False, True, False, False, True, True, False],
            [False, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, True],
            [False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, False],
            [True, True, True, False, True, True, False, False, False, True, True, False, False, False, False, False, False, True, False, True],
            [True, False, False, True, True, False, False, False, True, True, True, True, False, True, False, True, True, True, True, False],
            [True, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False, False, False],
            [False, False, True, False, False, False, True, True, False, True, True, True, True, True, True, True, False, False, False, False],
            [True, True, False, True, False, True, False, True, False, True, True, True, False, False, False, True, True, False, True, False] ]

# constants - also global
FULLHOUSE: int = len(evening) * len(evening[0]) # or = 200
MAXROWS:int = len(evening)
MAXCOLUMNS:int = len(evening[0])

def countBooked() -> int:
    counter: int = 0                      # to count the free seats
    for row in range(MAXROWS):
        for column in range(MAXCOLUMNS):
            if evening[row][column]:    # no need for evening[row][column] == True as evening already contains booleans
                counter = counter + 1
            # endif
        # next column
    # next row
    return counter

# book the seats
def book(seatsToBook: int):
    while seatsToBook > 0:
        for row in range(MAXROWS):
            for column in range(MAXCOLUMNS):
                if seatsToBook == 0:
                    return
                if seatsToBook > 0 and evening[row][column] == False:
                    evening[row][column] = True # change seat to booked
                    print(f'Booked seat @ row #{row+1} and column#{column+1}.')
                    seatsToBook = seatsToBook - 1
                # endif                
            # next column
        # next row
    # next seats                

def theatreLayout():
    print('\n   1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n')
    for row in range(MAXROWS):
        print( (row+1) % 10, end='  ')
        for column in range(MAXCOLUMNS):
            if evening[row][column]:
                print('B', end=' ')
            else:
                print('A', end=' ')
            # endif
        # next column
        print() # go to next row
    # next row
    print('\nB = Booked; A = Available')

### main ###

# We use the houseFull flag and the while loop to keep booking util the house is full
houseFull: bool = False
while not houseFull:
    theatreLayout() # to visualise the theatre bookings
    # input and validation of required seats
    bookedSeats:int = countBooked()
    availableSeats:int = FULLHOUSE - bookedSeats
    print(f'Number of seats already booked for the evening = {bookedSeats}' )
    print(f'Available seats left = {availableSeats}.')
        
    if bookedSeats == FULLHOUSE:
        print('Sorry!!! House full.')
        houseFull = True
        break
    
    print('Seats are allocated in order from those available. A row or seat number cannot be requested.')
        
    seatsRequired:int = int(input('Number of seats required? '))
    print()
    # 0 exits the loop and ends the program
    if seatsRequired == 0:
        break
    
    # validation - range check
#     while seatsRequired < 0 or seatsRequired > 4:
#         print('Only up to and including four seats can be booked at one time.')
#         seatsRequired = int(input('Number of seats required? '))
    # endwhile
    
    if seatsRequired > availableSeats:
        print(f'Not enough available seats, sorry! Only {availableSeats} left.\n')
    else:
        book(seatsRequired)
        #availableSeats  = FULLHOUSE - countBooked()
        #print()
        #theatreLayout()
        #print(f'Available seats left = {availableSeats}.')
    # endif
# endwhile